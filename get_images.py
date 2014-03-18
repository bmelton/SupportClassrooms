import requests
from school.models import School

def get_image():
    # school_address = "Southshore Elementary, 21032"
    for school in School.objects.all():
        school_address = "%s,%s" % (school.name, school.zipcode)
        print school_address, school.uid
        url = "http://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=13&size=2000x900&maptype=roadmap&sensor=false&scale=2" % (school_address)

        r = requests.get(url, stream=True)
        path = "./static/images/%s/%s.png" % (school.state, school.uid)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r.iter_content():
                    f.write(chunk)
