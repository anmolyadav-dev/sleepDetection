import ssl
import smtplib
from email.message import EmailMessage

email_sender = 'quicksilvers6969@gmail.com'
email_password = 'kxbb iagm ubta jqds'
email_receiver = ''

Subject = 'Stay Alert and Engaged in Online Classes!'
body = '''

I hope this email finds you well. As we navigate the challenges of virtual learning, it's crucial to maintain focus and active participation during online classes. Here are some friendly reminders to help you stay alert and avoid the temptation of dozing off:

Create a Dedicated Workspace: Designate a quiet and well-lit area for your virtual classes. A comfortable and distraction-free environment can significantly enhance your focus and attention.

Engage Actively: Participate in class discussions, ask questions, and contribute to activities. Active involvement not only reinforces your understanding of the material but also helps keep your mind sharp and attentive.

Take Regular Breaks: Incorporate short breaks between classes to stretch, move around, or grab a healthy snack. These breaks can rejuvenate your energy levels and prevent feelings of fatigue.

Use Interactive Tools: If available, make the most of interactive tools provided during online classes. Polls, quizzes, and group discussions can add an element of engagement to your virtual learning experience.

Prioritize Adequate Sleep: Ensure you get enough rest the night before classes. A well-rested mind is more alert and receptive to learning. Establishing a consistent sleep routine is crucial for maintaining focus during class hours.

Remember, your active participation and attentiveness contribute to a positive online learning environment for everyone. Feel free to reach out if you have any concerns or need additional support.

Wishing you a successful and engaging virtual learning experience!

Best regards

'''
def SendEmail(email_receiver) :
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = Subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
