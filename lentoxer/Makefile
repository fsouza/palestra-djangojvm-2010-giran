classpath_command=CLASSPATH=`pwd`/lib/mysql-connector-java-5.1.13-bin.jar

all: clean war

syncdb:
	@$(classpath_command) jython manage.py syncdb

run:
	@$(classpath_command) jython manage.py runserver

war:
	@$(classpath_command) jython manage.py war --include-java-libs=`pwd`/lib/mysql-connector-java-5.1.13-bin.jar --verbosity=2

shell:
	@$(classpath_command) jython manage.py shell

sql:
	@echo 'Gerando SQL, aguarde...'
	@$(classpath_command) jython manage.py sql core auth contenttypes sessions sites > dump.sql
	@echo 'Feito, verifique o arquivo dump.sql'

clean:
	@find . -name "*.class" -exec rm -f {} \;
	@echo 'Done.'
