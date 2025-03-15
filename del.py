import json
import os
from datetime import datetime

import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
django.setup()

# Now you can import Django models after django.setup()
from core.models import Award, Certificate, Course, Image, Project, Skill

# Now you can import Django models
# For example:
# from your_app.models import YourModel


# Assuming you have the models defined as in your provided code
# and you have a Django environment set up.  This code *must* be run
# within a Django context (e.g., using `manage.py shell` or within a
# Django view/management command).  It will *not* work as a standalone
# Python script without the Django ORM.


def create_data_from_json(json_data):
    """
    Creates Image, Skill, and Project objects from the given JSON data.
    """
    for item in json_data:
        if True:
            # Extract relevant fields for Project
            description = item.get("description")
            title = item.get("title")
            links = item.get(
                "links", []
            )  # Default to empty list if "links" is missing
            date_str = item.get("date", {}).get("$date")

            # Handle date parsing (important!)
            start_month = None
            start_year = None
            end_month = None
            end_year = None

            if date_str:
                date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                start_month = date_obj.month
                start_year = date_obj.year
                # Assuming projects don't span across years for simplicity in this example
                # You might need more complex logic if end_month/end_year are different
                end_month = start_month
                end_year = start_year

            # Create the Project object
            project = Project.objects.create(
                name=title,
                description=description,
                link=";".join(links)
                if links
                else None,  # Join links with a semicolon
                start_month=start_month,
                start_year=start_year,
                end_month=end_month,
                end_year=end_year,
            )

            # Handle Images
            image_paths = item.get("images", [])  # Default to empty list
            for image_path in image_paths:
                #  IMPORTANT:  This assumes the images are ALREADY in your
                #  'media/images/' directory.  This code does *NOT* handle
                #  downloading or saving the images from URLs.  You would
                #  need to do that separately (e.g., using `requests` and
                #  saving the file to the correct location).
                #  Also, it assumes the image paths are relative to your
                #  MEDIA_ROOT.
                try:
                    image = Image.objects.create(image=image_path.lstrip("/"))
                    project.images.add(image)
                except Exception as e:
                    print(f"Error creating image {image_path}: {e}")
                    #  Consider more robust error handling (e.g., logging,
                    #  skipping the image, etc.)

            # Handle Skills (using tags)
            tags_str = item.get("description", "")  # Use description for tags
            if "Tags:" in tags_str:
                tags_part = tags_str.split("Tags:")[1].strip()
                tags = [tag.strip() for tag in tags_part.split(",")]
                for tag in tags:
                    skill, created = Skill.objects.get_or_create(
                        name=tag
                    )  # Use get_or_create
                    project.skills.add(skill)

            print(f"Created project: {project.name}")


def main():
    # Read the JSON data from file
    try:
        with open("portfolio.posts.json", "r") as file:
            json_data = json.load(file)
            print("my json length is", len(json_data))

        # Pass the data to our function
        print(f"Found {len(json_data)} items in JSON file")
        create_data_from_json(json_data)
    except FileNotFoundError:
        print("Error: portfolio.posts.json file not found")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in portfolio.posts.json")
    except Exception as e:
        print(f"Error processing JSON data: {str(e)}")

    # Courses
    Course.objects.create(
        name="Django Full Stack Bootcamp",
        link="http://ude.my/UC-760f76af-0203-4535-9188-88fcd54684cf",
        description='32-hour Django course that I went through in a week to develop "Minas Gerais Tourism", my FBLA project that earned 1st place in the state of NJ.',
        association="Udemy",
        start_month=7,
        start_year=2022,
    )

    Course.objects.create(
        name="Crash Course on Python",
        link="http://coursera.org/verify/HQDZ78NMH4Z3",
        description="Successfully completed an online non-credit course authorized by Google and offered through Coursera. I was able to complete all the material during a one week free trial as preparation to begin teaching Python at AiGoLearning.",
        association="Google",
        start_month=12,
        start_year=2020,
    )

    # Certificates
    Certificate.objects.create(
        name="FutureHacks I Certificate of Appreciation",
        link="https://drive.google.com/file/d/1zFvu7X7gxiC3YFymmTKQe4_TJOaTGM3G/view?usp=sharing",
        description="Volunteered to host a one hour workshop of Python at AiGoLearning's Hackathon",
        association="AiGoLearning",
        start_month=3,
        start_year=2021,
    )

    Certificate.objects.create(
        name="FutureHacks II Certificate of Appreciation",
        link="https://drive.google.com/file/d/110oWOjeuDxyV1MV11DBUFxa9YIJZoFPM/view?usp=sharing",
        description="Volunteered to host a one hour workshop of Python at AiGoLearning's Hackathon",
        association="AiGoLearning",
        start_month=9,
        start_year=2021,
    )

    Certificate.objects.create(
        name="AiGoLearning Certificate of Volunteering",
        link="https://drive.google.com/file/d/1hojgui8NLlmuVKRe1HFAwrJHrcBL6EKA/view?usp=sharing",
        description="Volunteered over 240 hours at AiGolearning through countless activities such as teaching, workshops, developing, leading, etc.",
        association="AiGoLearning",
        start_month=9,
        start_year=2022,
    )

    Certificate.objects.create(
        name="Python Certificate of Training",
        link="https://drive.google.com/file/d/1ycE8DwrNKd-eL4C90NyFF6iOK_3HBloX/view?usp=sharing",
        description="Successfully passed the AiGoLearning evaluation to be a Python teacher.",
        association="AiGoLearning",
        start_month=12,
        start_year=2020,
    )

    Certificate.objects.create(
        name="Certificate of Completion Road Test",
        link="https://drive.google.com/file/d/1LoB_m8KSO7fAYve0n6ni3ls2oyhJ5dw_/view?usp=sharing",
        description="Successfully demonstrated financial skills in road test for personal finance.",
        association="Academy for Information Technology",
        start_month=5,
        start_year=2021,
    )

    Certificate.objects.create(
        name="IC3 Digital Literacy Certification",
        link="https://drive.google.com/drive/folders/1tD91kCjoFAOd6Z7VXI7obkSqXGoU2Y1p?usp=sharing",
        description="",
        association="Academy for Information Technology",
        start_month=12,
        start_year=2019,
    )

    Certificate.objects.create(
        name="Microsoft Office Specialist",
        link="https://drive.google.com/drive/folders/1p-ErEoJ7ngjkP_LHfyF98TGLMTDoZ-bY?usp=sharing",
        description="Certified Office specialist in Word (expert), Excel, Powerpoint, and Access.",
        association="Academy for Information Technology",
        start_month=6,
        start_year=2020,
    )

    Certificate.objects.create(
        name="Java Foundations",
        link="https://drive.google.com/file/d/1-5-FrX0yvR5wb1En45DhSx8f7ecxiTQe/view?usp=sharing",
        description="This certifies me as recognized by Oracle Corporation as Oracle Certified. In the test, I have the highest score in our grade together with another peer.",
        association="Academy for Information Technology",
        start_month=6,
        start_year=2022,
    )

    # Awards
    Award.objects.create(
        name="National Hispanic Recognition Program",
        link="https://drive.google.com/file/d/1YkGOLh4LMeILAhe2RE8969UAAcuP1uly/view?usp=sharing",
        description="",
        issuer="CollegeBoard",
        start_month=8,
        start_year=2022,
    )

    Award.objects.create(
        name="InnerView Volunteering Recognition",
        description="My school counselor recommended I logged my teaching hours on InnerView. There, I had the opportunity to be recognized for teaching coding for over 50 hours between June 1st, 2020 and April 15, 2021. Since then I have more than doubled that time.",
        link="https://www.linkedin.com/posts/rafael-almeida-386bb0202_computerscience-stem-codingforkids-activity-6775880270274011136-CVP1?utm_source=share&utm_medium=member_desktop",
        issuer="AiGoLearning",
        start_month=4,
        start_year=2021,
    )

    Award.objects.create(
        name="Victory Lane Certificate of Achievement",
        link="https://drive.google.com/file/d/1FQ5Yb8nkCGtH_NeUszPuxP_D71MpIU6p/view?usp=sharing",
        description="I demonstrated mastery of financial skills in the road test for personal finance. I did so by creating a program that told me exactly what to do on the challenge every day. I nearly achieved a perfect score.",
        issuer="Academy for Information Technology",
        start_month=5,
        start_year=2021,
    )

    Award.objects.create(
        name="AP Scholar Award",
        link="https://drive.google.com/file/d/1oGzfzItUjRbOx7IvVJTluCkMmZC5o68c/view?usp=sharing",
        description="I have earned the AP® Scholar Award which recognizes exemplary college-level achievement, for scoring 3 or higher on three or more AP Exams: Calculus AB, Computer Science A, Capstone Seminar. ",
        issuer="CollegeBoard",
        start_month=7,
        start_year=2022,
    )

    Award.objects.create(
        name="Teacher of the Week for AiGoLearning",
        description="In my first week teaching at AiGoLearning, I am glad to say that my competence has been noticed as I was selected to be teacher of the week and even got interviewed by AiGoLearning's journalist.",
        link="https://www.linkedin.com/posts/rafael-almeida-386bb0202_computerscience-stem-codingforkids-activity-6775880270274011136-CVP1?utm_source=share&utm_medium=member_desktop",
        issuer="AiGoLearning",
        start_month=3,
        start_year=2021,
    )

    Award.objects.create(
        name="State Champion Future Business Leaders of America",
        description="I placed 1st in the Coding and Programming FBLA competition in the state of NJ, qualifying to go to nationals. I was not able to go to nationals, however, due to the high costs and its overlapping dates with Thrive Scholars",
        link="",
        issuer="Academy for Information Technology",
        start_month=3,
        start_year=2022,
    )

    Award.objects.create(
        name="National Honor Society",
        description="I am proud that my academic achievements and, most importantly, the care I have for my community has been recognized, making me a member of the National Honor Society during high school and middle school in Junior Honor Society.",
        link="https://drive.google.com/file/d/1vD5buGoNunuYmfTEDwsoYqatpCHlB_3X/view?usp=sharing",
        issuer="Academy for Information Technology",
        start_month=3,
        start_year=2022,
    )

    Award.objects.create(
        name="Student of the Month",
        description="I was selected to be the junior student of the month for November.",
        link="https://drive.google.com/file/d/1L9O8iRgyYLuIshnc2_C6RMu_Jn4JpMUX/view?usp=sharing",
        issuer="Academy for Information Technology",
        start_month=11,
        start_year=2021,
    )

    Award.objects.create(
        name="Computer Science Departmental Award",
        description='I earned the Academy for Information Technology Computer Science departmental award for my "deep curiosity in class, outstanding excellence, and long-lasting contributions to the department." I took all Computer Science courses offered, getting all As. Most importantly, I invested over 400 hours in tutoring students, developing software for our school, revitalizing our coding club as President, and working closely with staff to improve CS education. I stood out among 74 other stellar CS students because of my technical prowess and a keen eye for endeavors where my skills would generate the most impact.',
        link="",
        issuer="Academy for Information Technology",
        start_month=6,
        start_year=2023,
    )

    # Achievements (creating as Awards since there's no specific Achievement model)
    Award.objects.create(
        name="PSAT Score",
        description="1390, (EBRW: 690, Math: 700). Though I di not qualify in NJ for the National Merit Program, I feel accomplished that I was in the 99th percentile without studying for the PSAT, as recommended by our school.",
        link="",
        issuer="CollegeBoard",
        start_month=1,
        start_year=2021,
    )

    Award.objects.create(
        name="United States of America Computing Olympiad",
        description="Silver division, placing 1837 out of 9484 participants. However, continuously studying hard to decrease my placing and to keep up with the ever more challenging problems. ",
        link="",
        issuer="Academy for Information Technology",
        start_month=2,
        start_year=2022,
    )

    Award.objects.create(
        name="NJSLA Score",
        description="Though not a high-stakes test, I feel accomplished scoring 300/300. With the NJ and my school's average being 166 and 258, respectively. ",
        link="https://drive.google.com/file/d/13tiBArATZV0DvST2pYhwC68UB8eW2br7/view?usp=sharing",
        issuer="Academy for Information Technology",
        start_month=5,
        start_year=2022,
    )

    Award.objects.create(
        name="SAT Score",
        description="1560, (EBRW: 770, Math: 790). After 3,000 answered questions and over 100 hours of studying, I increase my SAT score by exactly 200 points since my first SAT. I got a 1530, (EBRW: 740, Math 790), on August of 2022, and everyone thought I was crazy when I said I was taking it again. They did not want me to risk getting a lower score. But, I knew I had more to give.",
        link="",
        issuer="CollegeBoard",
        start_month=10,
        start_year=2022,
    )

    Award.objects.create(
        name="High Honor Roll",
        description="I am proud to say that I have never gotten a final B grade during my high school career, qualifying me for high honor roll every marking period so far.",
        link="",
        issuer="Academy for Information Technology",
        start_month=6,
        start_year=2022,
    )


if __name__ == "__main__":
    main()
