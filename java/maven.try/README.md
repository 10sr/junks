j/java/maven.try
================


Check installing

    mvn --version


Maven Usage
-----------

    mvn architype:create

    mvn compile

    mvn test

    mvn package

    mvn install

    mvn deploy



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
