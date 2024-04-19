def student(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

student(name="Shahid",course = "MCA")
student(name="Nikie")
student(name="komal",course="MBA",location="Delhi")