# AWS Lambda Implementation with gRPC and REST

- __Author__: [Lakshmanan Meiyappan](https://laxmena.com)
- __Email__: [lmeiya2@uic.edu](mailto:lmeiya2@uic.edu)

This project uses AWS Lambda to implement a REST and gRPC server, built with Scala and sbt.

## Dependencies

- Scala 2.13.4
- SBT 1.5.2
- slf4j-api 2.0.0
- typesafe config 1.4.1
- aws-lambda-java-core 1.2.1
- aws-lambda-java-events 3.10.0
- scalapb-runtime-grpc

## Functionality

LogProcessing Map-Reduce comprises Four Map-Reduce Tasks.

- __LogLevel Frequency__: Compute Count for each Log Level across all input files.
- __Most Error in TimeInterval__: Find Time Intervals with most errors, results in descending order.
- __Longest Substring matching Regex__: Length of Longest Substring that matches a Regular Expression.
- __LogLevel Frequency Distribution in TimeIntervals__: LogLevel distributions in specified TimeIntervals.

Users can inject Regex pattern in the Config files, and the Map-Reduce jobs will search for the pattern in the LogFiles
and produce results for the requested pattern.

See How to __Run LogProcessing MapReduce__ section for more instructions on how to execute this program.

## Documentation and Demo Video

Please find the __Documentation__ of this Project hosted in Github pages here: [LogProcessing Documentation](https://laxmena.github.io/LogProcessing-MapReduce/)

__Demo and Walk-through Video:__

[Running LogProcessing Map-Reduce on AWS EMR](https://youtu.be/et5_2hc6MWo)

[![LogProcessing AWS Video Demo](https://img.youtube.com/vi/et5_2hc6MWo/0.jpg)](https://youtu.be/et5_2hc6MWo)


## Report and Results

Detailed Report and results after executing the Map Reduce task can be found here: __[LogProcessing MapReduce Report](./report/README.md)__.

## How to Run "AWS-Lambda with gRPC and REST"?

### Creating compiled jar file
#### Step 1: Clone the Project
```bash
git clone https://github.com/laxmena/AWS-Lambda-with-gRPC-Rest.git
cd AWS-Lambda-with-gRPC-Rest
```

#### Step 2: Generate JAR File
```bash
sbt clean compile 
sbt test
sbt assembly
```
This command will generate a jar file in `target/scala-2.13.4/` directory

### How to Execute the MapReduce Jobs?


1. Connect to the remote hadoop master using putty or command line.
2. Transfer the Input Log Files and JAR file to remote machine. Copy the input files to the HDFS directory. (See Commands 1, 3 and 4 in __Useful commands__ section below.)
3. Run the Hadoop map reduce job by executing the following command:
    ```shell
    hadoop jar LogProcessing-MapReduce-assembly [input-path] [output-path] [job-key] [pattern-key]
    ```
4. On successful completion of Map-Reduce task, the results will be generated in the `[output-path]`. See commands 5 and 6 in __Useful commands__ section below to read the output.

List of available `[job-key]` and its associated Map-Reduce task:

| job-key | Map-Reduce Task | Supports Regex Search? |
|---------|-----------------|-------------------------------|
| log-frequency | LogLevel Frequency | &#x2718; |
| most-error | Most Error in TimeInterval | &#x2714; |
| longest-regex | Longest Substring matching Regex | &#x2714; |
| log-freq-dist | LogLevel Distribution in TimeIntervals | &#x2714; |

List of available `pattern-key` by Default:

|  key  | pattern | Description |
|-------|---------|-------------|
| pattern1 | .* | (Default) Matches Entire String |
| pattern2 | \\([^)\\n]*\\) | String enclosed within Parantheses |
| pattern3 | [^\\s]+ | String without any spaces |
| pattern4 | [\\d]+ | Consecutive Numbers |
| pattern5 | ([a-c][e-g][0-3] or [A-Z][5-9][f-w]){5,15} | Pattern1 or Pattern2 should repeat between 5 to 15 times, inclusive |

Different combinations of `job-key` and `pattern-key` can be used to execute Map-Reduce tasks.

Examples:
1. `hadoop jar LogProcessing-MapReduce-assembly-0.1.jar logprocess/input logprocess/longest-regex-1 longest-regex pattern1`
2. `hadoop jar LogProcessing-MapReduce-assembly-0.1.jar logprocess/input logprocess/log-freq-dist-3 log-freq-dist pattern3`
3. `hadoop jar LogProcessing-MapReduce-assembly-0.1.jar logprocess/input logprocess/logfrequency`
4. `hadoop jar LogProcessing-MapReduce-assembly-0.1.jar logprocess/input logprocess/mosterror most-error pattern5`

### Useful commands:

1. Transfer file from Local Machine to a Remote machine
    ```sh  
    scp -P 2222 <path/to/local/file> <username@remote_machine_ip>:<path/to/save/files>
    ```
2. Transfer directory from Local Machine to Remote machine
    ```sh  
    scp -P 2222 -r <path/to/local/directory> <username@remote_machine_ip>:<path/to/save/files>
    ```
3. Create HDFS Directory
    ```sh
    hadoop fs -mkdir <directory_name>
    ```
4. Add Files to HDFS
    ```shell
    hadoop fs -put <path/to/files> <hdfs/directory/path> 
    ```
5. Reading Hadoop Map-Reduce Output
    ```shell
    hadoop fs -cat <hdfs/output/directory>/*
    ```
6. Save Hadoop Map-Reduce output to Local file
   ```shell
   hadoop fs -cat <hdfs/output/directory>/* > filename.extension
   ```
7. Running JAR with multiple main classes
   ```shell
   hadoop jar <name-of-jar> <full-class-name> <input-hdfs-directory> <output-hdfs-directory> 
   ```
8. List files in HDFS Directory
   ```shell
    hdfs dfs -ls
    hdfs dfs -ls <directory/path>
   ```
9. Remove file or directory in HDFS
   ```shell
   hdfs dfs -rm -r <path/to/directory>
   hdfs dfs -rm <path/to/file>
   ```
