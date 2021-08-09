using System;
using System.Threading.Tasks;
using System.Net.Http;
using System.Text;
using System.Text.Json;


namespace console
{
    class Program
    {   
        static async Task Main(string[] args)
        {
            await Summarize();
        }

        private static async Task Summarize()
        {
            string jparams = "{\"text\":\"Amazon Elastic Compute Cloud (EC2) is a part of Amazon.com's cloud-computing platform, Amazon Web Services (AWS), that allows users to rent virtual computers on which to run their own computer applications. EC2 encourages scalable deployment of applications by providing a web service through which a user can boot an Amazon Machine Image (AMI) to configure a virtual machine, which Amazon calls an instance, containing any software desired. A user can create, launch, and terminate server-instances as needed, paying by the second for active servers – hence the term elastic. EC2 provides users with control over the geographical location of instances that allows for latency optimization and high levels of redundancy.In November 2010, Amazon switched its own retail website platform to EC2 and AWS.\"}";
            Console.WriteLine("Full text");
            Console.WriteLine(jparams);

            HttpClient Client = new HttpClient();
            Client.BaseAddress = new Uri("http://localhost:8000/summarize/");
            using var content = new StringContent(jparams, Encoding.UTF8, "application/json");

            var response = await Client.PostAsync((Uri)null, content);
            using var contentStream = await response.Content.ReadAsStreamAsync();
            var jsummarized = await JsonSerializer.DeserializeAsync<Summarized>(contentStream);
            var json = JsonSerializer.Serialize(jsummarized);

            Console.WriteLine($"Result: {json}");
        }

        class Summarized
        {
            public string summary { get; set; }
        }
    }
}
