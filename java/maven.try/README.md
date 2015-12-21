j/java/maven.try
================


Check installing

    mvn --version


Maven Usage
-----------

    mvn architype:generate

Generate a maven project in a new directory.


    mvn compile

Compile.


    mvn test

Run tests.

    mvn package

Create jar file in `target/` dir.


    mvn install

Install jar file locally so that other local projects install it.


    mvn deploy

Publish jar file to the remote repository.



Create new Maven project

    mvn -B archetype:generate \
      -DarchetypeGroupId=org.apache.maven.archetypes \
      -DgroupId=com.example \
      -DartifactId=sample


Repository
----------

Users can prepare their own repositories and publish products there.


Directory Structure
-------------------

Maven decides the standard directory structure.

Typically it looks like:

    .
    |-- pom.xml
    `-- src
        |-- main
        |   `-- java
        |       `-- com
        |           `-- example
        |               `-- App.java
        `-- test
            `-- java
                `-- com
                    `-- example
                        `-- AppTest.java


pom.xml
-------

File `pom.xml` is an important files that has properties about the project:

  * Project building
  * Libraries the project depends on
  * Configuration of plguins
