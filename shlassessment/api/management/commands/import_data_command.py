from django.core.management.base import BaseCommand
from api.models import shlModel  # Import your model

class Command(BaseCommand):
    help = 'Insert data into the shlModel table'

    def handle(self, *args, **options):
        data_to_insert=[{'title': 'Project 1', 'technologies': 'Python, HTML, CSS, Machine Learning, Deep Learning', 'frontend': 'HTML, CSS, JavaScript', 'backend': 'Python', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 2', 'technologies': 'Java Spring Boot, Hibernate, MySQL', 'frontend': 'React JS', 'backend': 'Java, Spring Boot, Hibernate', 'databases': 'MySQL', 'infrastructure': 'Not specified'}, {'title': 'Project 3 ', 'technologies': 'Java, HTML, CSS, JavaScript', 'frontend': 'React, HTML, CSS', 'backend': 'Java, Python Django, Flask', 'databases': 'MySQL, MongoDB, Postgres', 'infrastructure': 'AWS, Azure OCR, Apache, Docker'}, {'title': 'Project 4', 'technologies': 'Websockets, Redis, Channel layers', 'frontend': 'React', 'backend': 'Python Django, Django Rest', 'databases': 'MySQL', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 5', 'technologies': 'Python, Scrapy framework, MongoDB', 'frontend': 'React Native', 'backend': 'Python, Django', 'databases': 'MongoDB', 'infrastructure': 'Not Specified'}, {'title': 'Project 6', 'technologies': 'Postman, Docker, Jenkins, Java, Spring Boot', 'frontend': 'React, Angular', 'backend': 'Spring Boot, Java', 'databases': 'Not mentioned', 'infrastructure': 'Postman, Docker, Jenkins'}, {'title': 'Project 7', 'technologies': 'React JS, JWT Authentication, Local Storage', 'frontend': 'React JS, HTML, CSS, JavaScript', 'backend': 'Node JS', 'databases': 'MongoDB', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 8', 'technologies': 'Python, Django, API', 'frontend': 'No experience', 'backend': 'Python Django, API', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 9', 'technologies': 'React, Node, Java', 'frontend': 'React, Java, Angular, Node, JavaScript', 'backend': 'Node', 'databases': 'SQL', 'infrastructure': 'Not mentioned'}, {'title': 'Project 10', 'technologies': 'React JS, Redux, HTML, CSS, Bootstrap, Material UI, Socket.io, Python Django', 'frontend': 'React JS, HTML, CSS, Bootstrap, Material UI', 'backend': 'Python Django', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 11', 'technologies': 'React JS, Node JS, TNT database', 'frontend': 'HTML, CSS, JavaScript, React JS', 'backend': 'Node JS', 'databases': 'SQL, TNT', 'infrastructure': 'Not mentioned'}, {'title': 'Project 12', 'technologies': 'React JS, Mongo DB, MVC architecture', 'frontend': 'React JS', 'backend': 'Mongo DB', 'databases': 'Mongo DB', 'infrastructure': 'Not mentioned'}, {'title': 'Project 13', 'technologies': 'Python, Java, Redis, caching, pagination, liquibase', 'frontend': 'React, Next js', 'backend': 'Python Django and Spring frameworks', 'databases': 'Not Specified', 'infrastructure': 'Not Specified'}, {'title': 'Project 14', 'technologies': 'Python, AWS, JavaScript, Node JS, Docker', 'frontend': 'Angular, JavaScript, TypeScript', 'backend': 'Python, Java, Node JS, AWS Lambda functions', 'databases': 'SQL', 'infrastructure': 'Docker, AWS'}, {'title': 'Project 15', 'technologies': 'Java, Spring Framework', 'frontend': 'React', 'backend': 'Python, Django, Java, Spring Framework', 'databases': 'Not Mentioned', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 16', 'technologies': 'SQL, Cloud, Ecommerce, Haru, Spoke', 'frontend': 'React, Angular, Next.js', 'backend': 'SQL, MySQL, Oracle, Java, NoSQL', 'databases': 'SQL, MySQL, Oracle, NoSQL', 'infrastructure': 'Cloud platforms'}, {'title': 'Project 17', 'technologies': 'HTML, CSS, Node.js, SQL, MongoDB', 'frontend': 'HTML, CSS, React', 'backend': 'Node.js', 'databases': 'SQL, MongoDB', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 18', 'technologies': 'Java, Spring Boot, Angular, HTML, CSS, JavaScript, SQL', 'frontend': 'Angular, React, Next js', 'backend': 'Python Django, Spring', 'databases': 'SQL', 'infrastructure': 'HTTPD'}, {'title': 'Project 19', 'technologies': 'Machine learning, Linear and Logistic Regression', 'frontend': 'React, Angular', 'backend': 'Python Django, Java Spring', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 20', 'technologies': 'AWS, Node JS, Aurora DB, React, Python, TypeScript, JavaScript, CICD pipelines, ECS containers and topics', 'frontend': 'React', 'backend': 'Python, Node.js', 'databases': 'Aurora DB', 'infrastructure': 'AWS, ECS containers'}, {'title': 'Project 21', 'technologies': 'Django, Elasticview', 'frontend': 'React', 'backend': 'Django', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 22', 'technologies': 'Third Party APIs, Encryption and Decryption Algorithms', 'frontend': 'Angular, React, Next.js', 'backend': 'Node.js, Express', 'databases': 'Not Mentioned', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 23', 'technologies': 'Java, React/TypeScript', 'frontend': 'React, Next JS, Google Auth', 'backend': 'Java Spring Framework', 'databases': 'Not Specified', 'infrastructure': 'Not Specified'}, {'title': 'Project 24', 'technologies': 'Java, Python, SQL, MongoDB, Mongoose, Passport, React and Express', 'frontend': 'React JS (Beginner level, Self-rated 7/10)', 'backend': 'Java, Python, SQL (Self-rated 7/10)', 'databases': 'MongoDB, SQL', 'infrastructure': 'No information provided'}, {'title': 'Project 25', 'technologies': 'API, Event-based system', 'frontend': 'Reactjs', 'backend': 'Node JS, TypeScript, JavaScript', 'databases': 'Postgre SQL', 'infrastructure': 'Flutter'}, {'title': 'Project 26', 'technologies': 'React, React Native', 'frontend': 'React, React Native', 'backend': 'Not experienced, but a quick learner', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 27', 'technologies': 'Fitbit API, Isolation Forest Algorithm, Email Service', 'frontend': 'React', 'backend': 'Express, JavaScript', 'databases': 'Not Mentioned', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 28', 'technologies': 'Node JS, Puppeteer', 'frontend': 'JavaScript, React, Angular', 'backend': 'Node JS, Express, Python, Django', 'databases': 'Not mentioned', 'infrastructure': 'AWS'}, {'title': 'Project 29', 'technologies': 'Java, PostgreSQL', 'frontend': 'React', 'backend': 'Java', 'databases': 'PostgreSQL', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 30', 'technologies': 'React JS, Node JS, Express JS, MongoDB', 'frontend': 'HTML, CSS, JavaScript, jQuery', 'backend': 'PHP Codeigniter, Django', 'databases': 'MongoDB', 'infrastructure': 'Not specified'}, {'title': 'Project 31', 'technologies': 'Python Django, Flask, Spring Boot', 'frontend': 'ReactJS', 'backend': 'Python Django, Flask, Spring Boot', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 32', 'technologies': 'Node JS, JavaScript', 'frontend': 'Angular, React, Next js', 'backend': 'Node.js, Python Django', 'databases': 'Postman', 'infrastructure': 'Not mentioned'}, {'title': 'Project 33', 'technologies': 'Machine Learning, Random Forest, Extra Trees Regressor, Light Gradient Boosting', 'frontend': 'React JS', 'backend': 'Node JS, Express JS', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 34', 'technologies': 'CA framework, Python APIs, React', 'frontend': 'React', 'backend': 'Python, Node.js', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 35', 'technologies': 'Node JS, TypeScript, MongoDB', 'frontend': 'Not Specified', 'backend': 'Node JS', 'databases': 'MongoDB', 'infrastructure': 'Not Specified'}, {'title': 'Project 36', 'technologies': 'Java, Retrofit, MVC pattern', 'frontend': 'React Native', 'backend': 'Java', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 37', 'technologies': 'Multicast graded CNN model, Hybrid recommender system', 'frontend': 'Not mentioned', 'backend': 'Back-end frameworks and APIs', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 38', 'technologies': 'Java, JavaScript, Android app development, Firebase, Node.js, MongoDB, Postman', 'frontend': 'React, HTML, CSS', 'backend': 'Node.js', 'databases': 'MongoDB, Firebase', 'infrastructure': 'Firebase'}, {'title': 'Project 39', 'technologies': 'React JS, Node JS, HTML, CSS, JavaScript, EJS', 'frontend': 'React JS, HTML, CSS, JavaScript, EJS', 'backend': 'Node JS', 'databases': 'Not Mentioned', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 40', 'technologies': 'Javascript, SQL, Report Labs, React, Python Django, Java, Spring Boot, MySQL', 'frontend': 'React, HTML, CSS, JavaScript', 'backend': 'Python Django, Java, Spring Boot', 'databases': 'MySQL, Sequel Lite', 'infrastructure': 'Not mentioned'}, {'title': 'Project 41', 'technologies': 'DuckDuckGo API, React Native, TypeScript', 'frontend': 'React Native', 'backend': 'Prayat', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 42', 'technologies': 'HTML, CSS, JavaScript, Tableau, Power BI, SQL, C++', 'frontend': 'HTML, CSS, JavaScript, React JS', 'backend': 'None mentioned', 'databases': 'SQL', 'infrastructure': 'None mentioned'}, {'title': 'Project 43', 'technologies': 'Decentralized anomaly detection system, machine learning, attention mechanism', 'frontend': 'Angular, React, Next js', 'backend': 'Java, Spring Boot, JavaScript API', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 44', 'technologies': 'Azure APIs and SAS fulfillment APIs', 'frontend': 'Not mentioned', 'backend': 'Azure APIs and SAS fulfillment APIs', 'databases': 'SQL and NoSQL', 'infrastructure': 'Not mentioned'}, {'title': 'Project 45', 'technologies': 'Java, AWS DynamoDB', 'frontend': 'Learning React.js', 'backend': 'Java', 'databases': 'AWS DynamoDB', 'infrastructure': 'AWS'}, {'title': 'Project 46', 'technologies': 'HTML, CSS, JavaScript, React JS, Python Django, Express', 'frontend': 'HTML, CSS, JavaScript, React JS', 'backend': 'Python Django, Express', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 47', 'technologies': 'PHP, JavaScript, jQuery, HTML, CSS, Bootstrap, MySQL, Node JS, Express JS, MongoDB', 'frontend': 'Bootstrap, JavaScript, jQuery', 'backend': 'PHP, Node.js, Express.js', 'databases': 'MySQL, MongoDB', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 48', 'technologies': 'Python, Django, HTML, CSS, JavaScript', 'frontend': 'Angular, React, Next js', 'backend': 'Python Django, ASP.NET', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 49', 'technologies': 'KN algorithm, Flutter, Dart, Firebase', 'frontend': 'React', 'backend': 'Node.js', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 50', 'technologies': 'React, Node.js, API development', 'frontend': 'React', 'backend': 'Node.js', 'databases': 'MongoDB', 'infrastructure': 'Not mentioned'}, {'title': 'Project 51', 'technologies': 'Machine Learning, Smart Analysis', 'frontend': 'Not Specified', 'backend': 'Django', 'databases': 'Not Specified', 'infrastructure': 'Not Specified'}, {'title': 'Project 52', 'technologies': 'React, Django', 'frontend': 'React', 'backend': 'Django', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 53', 'technologies': 'Angular, React, Next js, Python Django, Express JS', 'frontend': 'Angular, React, Next js', 'backend': 'Python Django, Express JS', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 54', 'technologies': 'MongoDB, Express JS, Node JS, Java', 'frontend': 'Angular, React, Next js', 'backend': 'Python Django, Node.js', 'databases': 'MongoDB', 'infrastructure': 'Not mentioned'}, {'title': 'Project 55', 'technologies': 'Solidity', 'frontend': 'React.js', 'backend': 'Node.js', 'databases': 'MongoDB', 'infrastructure': 'Not provided'}, {'title': 'Project 56', 'technologies': 'NLTK library, Text BLOB and SVC', 'frontend': 'Not Mentioned', 'backend': 'Python', 'databases': 'Not Mentioned', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 57', 'technologies': 'React Jsonschema, Material React Table, Promises, Batch Functions', 'frontend': 'React, CJS, Redux, HTML, CSS', 'backend': 'Python', 'databases': 'Unknown', 'infrastructure': 'Messenger, Python, and machine learning'}, {'title': 'Project 58', 'technologies': 'TypeScript, Node.js', 'frontend': 'Angular', 'backend': 'Node.js', 'databases': 'Not Mentioned', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 59', 'technologies': 'React, Angular, Next.js, Python, Django, Flask, MongoDB, MySQL', 'frontend': 'React, Angular, Next.js', 'backend': 'Python, Django, Flask', 'databases': 'MongoDB, MySQL', 'infrastructure': 'Not Provided'}, {'title': 'Project 60', 'technologies': 'React, Python, SQL, Java, C', 'frontend': 'React', 'backend': 'Python Flask', 'databases': 'SQL', 'infrastructure': 'Not mentioned'}, {'title': 'Project 61', 'technologies': 'HTML, Form groups, S3 bucket', 'frontend': 'Angular, React, Next.js', 'backend': 'Spring Boot, Django', 'databases': 'MySQL', 'infrastructure': 'Engine X'}, {'title': 'Project 62', 'technologies': 'Python, Django, Django Rest Framework', 'frontend': 'No information provided', 'backend': 'Python, Django, Django Rest Framework', 'databases': 'No information provided', 'infrastructure': 'No information provided'}, {'title': 'Project 63', 'technologies': 'Lambda, AWS, API gateway, React', 'frontend': 'React, Redux', 'backend': 'Node.js, Python Django', 'databases': 'Not mentioned', 'infrastructure': 'AWS'}, {'title': 'Project 64', 'technologies': 'Django, React, Alpha Vantage API', 'frontend': 'React', 'backend': 'Python Django', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 65', 'technologies': 'JavaScript, HTML, CSS, Google Fonts, React Icon, Responsiveness', 'frontend': 'React, TypeScript', 'backend': 'Node, Express', 'databases': 'Not Mentioned', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 66', 'technologies': 'Digital Marketing', 'frontend': 'React, Angular', 'backend': 'Node', 'databases': 'Not Mentioned', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 67', 'technologies': 'React, Next JS, Node JS, Express, SQLite, MongoDB, Prisma', 'frontend': 'React, Next JS', 'backend': 'Node JS, Express', 'databases': 'SQLite, MongoDB, Prisma', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 68', 'technologies': 'Micro service architecture, Spring MVC, Spring Cloud', 'frontend': 'Interest in learning', 'backend': 'Java, Spring and Spring boot framework, REST APIs, micro services architecture', 'databases': 'Hadoop ecosystem', 'infrastructure': 'Micro services architecture'}, {'title': 'Project 69', 'technologies': 'TypeScript, FCM token, Socket IO, Google Descriptive APIs, Natural Language Processing', 'frontend': 'Not specified', 'backend': 'Python', 'databases': 'Not specified', 'infrastructure': 'Not specified'}, {'title': 'Project 70', 'technologies': 'Python, AI, ML', 'frontend': 'React JS', 'backend': 'Django, Python', 'databases': 'Not specified', 'infrastructure': 'Not specified'}, {'title': 'Project 71', 'technologies': 'Node JS, Express JS, MySQL, AWS, GitLab, Sonar, Swagger APIs', 'frontend': 'React', 'backend': 'Node.js, Express.js', 'databases': 'MongoDB, MySQL', 'infrastructure': 'AWS'}, {'title': 'Project 72', 'technologies': 'React JS, Akka microservices, Postgres, MongoDB, Sequel', 'frontend': 'Angular JS, React', 'backend': 'Scala, Akka, Play framework', 'databases': 'Postgres, MongoDB', 'infrastructure': 'Not specified'}, {'title': 'Project 73', 'technologies': 'Amazon SQS, Kafka', 'frontend': 'Angular, React, Next js', 'backend': 'Python Django', 'databases': 'Unspecified', 'infrastructure': 'Docker'}, {'title': 'Project 74', 'technologies': 'Postman, JUnit, threads, Jenkins, Docker', 'frontend': 'Angular, React, Next js', 'backend': 'Python Django, Spring Boot', 'databases': 'Not mentioned', 'infrastructure': 'Docker, Jenkins'}, {'title': 'Project 75', 'technologies': 'Cron job', 'frontend': 'React', 'backend': 'Not specified', 'databases': 'Not specified', 'infrastructure': 'Not specified'}, {'title': 'Project 76', 'technologies': 'JavaScript', 'frontend': 'JavaScript, React', 'backend': 'JavaScript', 'databases': 'Not Discussed', 'infrastructure': 'Not Discussed'}, {'title': 'Project 77', 'technologies': 'Django, Front-end and Back-end development', 'frontend': 'Basic knowledge', 'backend': 'Basic knowledge', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 78', 'technologies': 'ASP.NET, CSS, HTML, SQL Server', 'frontend': 'CSS, HTML, JavaScript, Ajax, Bootstrap', 'backend': 'ASP.NET MVC', 'databases': 'SQL Server', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 79', 'technologies': 'Java, WS, AWS, Lambda Functions, Cloud Watch, MongoDB, Express, React, Node JS', 'frontend': 'ReactJS', 'backend': 'NodeJS, ExpressJS', 'databases': 'MongoDB', 'infrastructure': 'AWS'}, {'title': 'Project 80', 'technologies': 'EF Core API, Angular, Azure', 'frontend': 'Angular JS', 'backend': '.Net, SQL', 'databases': 'SQL', 'infrastructure': 'Azure'}, {'title': 'Project 81', 'technologies': 'Machine learning, Linear regression', 'frontend': 'Undetermined', 'backend': 'Python, FAST API', 'databases': 'Undetermined', 'infrastructure': 'PyCharm'}, {'title': 'Project 82', 'technologies': 'JavaScript, External Libraries', 'frontend': 'Angular, React, Next js', 'backend': 'Python', 'databases': 'Not Mentioned', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 83', 'technologies': 'Machine Learning, Cosine Similarity', 'frontend': 'React, HTML, CSS, JavaScript', 'backend': 'Not mentioned', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 84', 'technologies': 'React, Node, Express, MongoDB, PostgreSQL, Django, Python', 'frontend': 'React', 'backend': 'Node, Express, Django, Python', 'databases': 'MongoDB, PostgreSQL', 'infrastructure': 'Not mentioned'}, {'title': 'Project 85', 'technologies': 'MongoDB, Angular, JavaScript, CSS, HTML, Python', 'frontend': 'Angular, React, Next.js', 'backend': 'Python Django, Fast APIs, Notes', 'databases': 'MongoDB', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 86', 'technologies': 'C++, Java, AWS, Spring Framework, J Unit, Machine Learning, Linux, AOP', 'frontend': 'JavaScript, React JS, HTML, CSS', 'backend': 'Node JS, Java, AWS, Spring Framework', 'databases': 'Not mentioned', 'infrastructure': 'AWS'}, {'title': 'Project 87', 'technologies': 'Open AI, Machine Learning Models, Python Libraries for Audio Conversion and Prompt Engineering', 'frontend': '4-5/10', 'backend': 'Python Django, 7-8/10', 'databases': 'Not Mentioned', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 88', 'technologies': 'Java, AWS Lambda', 'frontend': 'React', 'backend': 'Node.js, Express.js', 'databases': 'MongoDB', 'infrastructure': 'AWS'}, {'title': 'Project 89', 'technologies': 'MongoDB, Node JS, JavaScript, JWT, React Native', 'frontend': 'Reactjs, React Native', 'backend': 'Node.js, Express', 'databases': 'MongoDB, PostgreSQL', 'infrastructure': 'Knowledge not specified'}, {'title': 'Project 90', 'technologies': 'Pega, Python Node JS, Theme Cosmos', 'frontend': 'Python Node JS', 'backend': 'No prior experience with backend frameworks', 'databases': 'Not mentioned', 'infrastructure': 'Not mentioned'}, {'title': 'Project 91', 'technologies': 'React, Next.js, Python Django, Node.js, Express.js', 'frontend': 'React, Next.js', 'backend': 'Python Django, Node.js, Express.js', 'databases': 'Unknown', 'infrastructure': 'Unknown'}, {'title': 'Project 92', 'technologies': 'Machine Learning, Front-end and Backend Frameworks, AWS', 'frontend': 'Unknown', 'backend': 'Unknown', 'databases': 'Unknown', 'infrastructure': 'AWS'}, {'title': 'Project 93', 'technologies': 'JavaScript, HTML, CSS, Bootstrap, Express JS, Node JS', 'frontend': 'React, Redux, HTML, JavaScript, CSS, Bootstrap', 'backend': 'Express JS, Node JS', 'databases': 'MongoDB', 'infrastructure': 'Not provided'}, {'title': 'Project 94', 'technologies': 'CSS, HTML, CSS, JavaScript, Python, MySQL', 'frontend': 'Angular, React, Next js', 'backend': 'No Experience', 'databases': 'MySQL', 'infrastructure': 'No Experience'}, {'title': 'Project 95', 'technologies': 'React JS, Redux, React Hooks', 'frontend': 'HTML, CSS, JavaScript, React JS', 'backend': 'Node JS, C&C', 'databases': 'Not provided', 'infrastructure': 'Not provided'}, {'title': 'Project 96', 'technologies': 'React JS, Node.js', 'frontend': 'React JS', 'backend': 'Node.js (Learning)', 'databases': 'Not Mentioned', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 97', 'technologies': 'Mongoose, React JS, Node JS', 'frontend': 'React JS', 'backend': 'Node JS', 'databases': 'Mongoose', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 98', 'technologies': 'Open pose, MRCP CNN, Pandas, scikit learn, Python', 'frontend': 'HTML, JavaScript, jQuery, CSS', 'backend': 'Python, Django', 'databases': 'MySQL, MSSQL', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 99', 'technologies': 'React.js, Redux, Schema UI, Config one UI, Live Swiggy API, Conflict one UI', 'frontend': 'React.js', 'backend': 'Willing to learn', 'databases': 'Good understanding of data structures and algorithms', 'infrastructure': 'Not Mentioned'}, {'title': 'Project 100', 'technologies': 'Front-end and Back-end frameworks', 'frontend': '7.5/10', 'backend': '08-Oct', 'databases': 'Not Mentioned', 'infrastructure': 'Azure DevOps'}]
        for data in data_to_insert:
            shlModel.objects.create(
                title=data["title"],
                technologies=data["technologies"],
                frontend=data["frontend"],
                backend=data["backend"],
                databases=data["databases"],
                infrastructure=data["infrastructure"]
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created project: {data["title"]}'))