# Japanese Aphasia Web App for Training and Treatment
**Author**: Jakarin Chonchumrus &emsp; **Supervisor**: Dr. Mio Sakuma


## Introduction
At present, various technologies have been invented and used in daily life. The most popular technology at this moment is the “Web App”.

Web application or web app is software that runs in your web browser on every platform. It has many utilities such as recruiting jobs (LinkedIn), social media (Facebook and Instagram), file transfer or cloud services (Dropbox), and others. But there is a little bit of medical and increasing of elderly with Aphasia symptoms. Therefore, we should find a solution to this problem.
The author created the Japanese Aphasia Web app for training and treatment. It is for treating Aphasia patients with testing and evaluation by Japanese speech therapists.

## Background
[Aphasia symptoms][2] are a loss of language function, such as listening, speaking, reading, and writing. It is due to injury of the brain's language function area. It is one of the symptoms of higher brain function disorders caused by cerebrovascular disorders such as cerebral hemorrhage and cerebral infarction or traffic accidents and others.

[As the population ages in Japan, the number of Aphasia patients is increasing][5].
 
<img src="/static/screenshot/symptoms.png">
<p style="text-align:center;"><i>Figure 1: Example of Aphasia symptoms</i></p>

This web app testing and evaluation by speech therapists are professionals who identify the mechanisms of language disorders, evaluate eating and swallowing disorders, and provide training and support as needed.


## Design
The author designed a simple user interface for patients or therapists with dashboards and icons.

This web app has different roles for authorization in this web app. The first role is the therapist. They can add courses and questions for their patient. Next, the patient can take a course and watch their marks for each quiz. Finally, the last role is admin can approve the therapist and access the database such as name, age, phone number, and therapist salary.

<img style="border-radius: 5px;" src="/static/screenshot/therapist_page.png">
<div align="center"><i>Figure 2: Dashboard page (Therapist)</i></div>
 
<img style="border-radius: 5px;" src="/static/screenshot/question_page.png">
<p style="text-align:center;"><i>Figure 3: Example of question page</i></p>

The speech therapist designed questions for each patient. It is a multiple-choice test that is easy to answer and doesn't take long. 

## Implementation
JP Aphasia web using the Python language with Django framework and SQLite database
The frontend part uses Hypertext Markup Language or HTML with [Django Widget Tweaks][6]. It is for decorating and adding features to your web page looks like Bootstrap CSS, but it is easier than CSS and suitable for using Django.

The backend part uses [Python language][3] and [Django framework][1]. It has many systems as authentication for login or registering the account, authorization for separate roles to do each activity on the web, a management system for adding/updating/removing any data, and a dashboard system for displaying information. Programming technique uses functional components for making readable code and easy testing.

The database part uses [SQLite][4]. It is fast for R/W data and suitable for uncomplex databases. It keeps the personal data of the account after hashing method.
 
<img style="border-radius: 5px;" src="/static/screenshot/admin_page.png">
<p style="text-align:center;"><i>Figure 4: Dashboard page (Admin)</i></p>
 
<img style="border-radius: 5px;" src="/static/screenshot/db_page.png">
<p style="text-align:center;"><i>Figure 5: Database page (Admin)</i></p>

## Conclusion
This project proposes a Japanese Aphasia Web App for Training and Treatment. The web uses a simple user interface with dashboards and icons using HTML with Django Widget Tweaks. The system has an authorization and authentication system for separating each activity as therapists, patients, and admin. It manages the treatment courses of Aphasia patients with a multiple-choice question created by the speech therapists using Python language with the Django framework and SQLite database for keeping the personal data of the account after hashing method.

## Acknowledgments
The author was impressed by collaborating with Dr. Mio Sakuma and lab members in Dr. Sakuma's laboratory within the National Institute of Technology, Sendai College (SNCT) in Japan by the opportunity and scholarship of King Mongkut's Institute of Technology Ladkrabang (KMITL).

## References
- Django Software Foundation, 2023, “Django documentation”, Retrieved Jun 2023, From https://docs.djangoproject.com/en/4.2/
- Mayo Clinic, 2022, “Aphasia”, Retrieved Jun 2023, From https://www.mayoclinic.org/diseases-conditions/aphasia/symptoms-causes/syc-20369518
- Python Software Foundation, 2023, “Python documentation”, Retrieved Jun 2023, From https://docs.python.org/3/
- SQLite Consortium, 2023, “SQLite”, Retrieved Jun 2023, From https://www.sqlite.org
- Sumiko Sasanuma, 1993, “Aphasia Treatment in Japan”, Retrieved Jun 2023, From https://link.springer.com/chapter/10.1007/978-1-4899-7248-4_8
- Vitor Freitas, 2015, “How to Use Django Widget Tweaks”, Retrieved Jun 2023, From https://simpleisbetterthancomplex.com/2015/12/04/package-of-the-week-django-widget-tweaks.html


[1]: https://docs.djangoproject.com/en/4.2/ "“Django Documentation"
[2]: https://www.mayoclinic.org/diseases-conditions/aphasia/symptoms-causes/syc-20369518 "Aphasia"
[3]: https://docs.python.org/3/ "Python Documentation"
[4]: https://www.sqlite.org "SQLite"
[5]: https://link.springer.com/chapter/10.1007/978-1-4899-7248-4_8 "Aphasia Treatment in Japan"
[6]: https://simpleisbetterthancomplex.com/2015/12/04/package-of-the-week-django-widget-tweaks.html "How to Use Django Widget Tweaks"
