# transformer-demo

Send text to pretrained model of choice

{"text":"Amazon Elastic Compute Cloud (EC2) is a part of Amazon.com's cloud-computing platform, Amazon Web Services (AWS), that allows users to rent virtual computers on which to run their own computer applications. EC2 encourages scalable deployment of applications by providing a web service through which a user can boot an Amazon Machine Image (AMI) to configure a virtual machine, which Amazon calls an instance, containing any software desired. A user can create, launch, and terminate server-instances as needed, paying by the second for active servers – hence the term elastic. EC2 provides users with control over the geographical location of instances that allows for latency optimization and high levels of redundancy.In November 2010, Amazon switched its own retail website platform to EC2 and AWS."}

Result:

{"summary":"Amazon Elastic Compute Cloud (EC2) is a part of Amazon.com\u0027s cloud-computing platform. it allows users to rent virtual machines on which to run their own computer applications. EC2 provides a web service through which a user can boot an Amazon Machine Image (AMI) to configure a virtual machine."}



## summarizer
$ uvicorn main:app --reload

$ curl -X POST localhost:8000/summarize/ -H "accept: applicaion/json" -H "Content-Type: application/json" -d @./article.json


## console
$ dotnet run --project console/console.csproj











