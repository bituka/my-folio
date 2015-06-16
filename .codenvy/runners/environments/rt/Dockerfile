FROM codenvy/jdk7
RUN mkdir /home/user/app /home/user/sdk
RUN wget -P /home/user/ --quiet http://repo.maven.apache.org/maven2/com/google/appengine/appengine-java-sdk/1.9.10/appengine-java-sdk-1.9.10.zip
RUN unzip /home/user/appengine-java-sdk-1.9.10.zip -d /home/user && cp -r /home/user/appengine-java-sdk-1.9.10/* /home/user/sdk && \
    rm -r /home/user/appengine-java-sdk-1.9.10.zip /home/user/appengine-java-sdk-1.9.10/
﻿ENV CODENVY_APP_PORT_8080_HTTP 8080
EXPOSE 8080
﻿WORKDIR /home/user/sdk/bin/
ADD $app$ /home/user/app/
﻿﻿RUN sudo chown -R user:user /home/user/app/WEB-INF/  
CMD ./dev_appserver.sh -a 0.0.0.0 /home/user/app