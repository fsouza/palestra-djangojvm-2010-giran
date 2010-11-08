classpath_command=CLASSPATH=$CLASSPATH:`pwd`/lib/mysql-connector-java-5.1.13-bin.jar

all: clean war

syncdb:
	@$(classpath_command) jython manage.py syncdb

runserver:
	@$(classpath_command) jython manage.py runserver

war:
	@$(classpath_command) jython manage.py war

clean:
	@find . -name "*.class" -exec rm -f {} \;
	@echo 'Done.'
