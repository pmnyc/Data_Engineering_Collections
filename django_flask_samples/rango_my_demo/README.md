Rango
==========

Tango with Django Web Application Demo

# Prerequisites
* $`sudo apt-get install curl`
* Install pyenv $`url -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash`
* Add path information. $`nano ~/.bashrc`
```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
* $`sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm`
* $`pyenv install 2.7.11`
  * Change local or global version of python $`pyenv versions`, and $`pyenv global 2.7.11`
* If $`echo $PYTHONPATH` shows no PYTHONPATH is added to PATH, then one needs to use $`python -c 'import site; print(site.getsitepackages()[0])'` to get its path and add export that path to $`export PYTHONPATH=$PYTHONPATH:<PATH_TO_SITE-PACKAGES>`, where `<PATH_TO_SITE-PACKAGES>`.
* Install setuptools $`wget https://bootstrap.pypa.io/ez_setup.py -O - | python`
* Install pip $`sudo easy_install pip`
* Install Django $`sudo pip install -U django==1.9`
* Install python imaging library $`sudo pip install pillow`
* Run $`pip list` to get list of packages installed. Export it out using $`pip freeze > requirements.txt`. When one needs to install pacakges of same versions on another computer, use $`sudo pip install -r requirements.txt`
* To run the whole python application within a specified environment, run $`pip install virtualenv` and $`sudo pip install virtualenvwrapper ; pip install virtualenvwrapper ; export WORKON_HOME=~/Envs ; mkdir -p $WORKON_HOME` to get virtual environment set up.
* To start the virtual environment, run $`source /usr/local/bin/virtualenvwrapper.sh`.
  * To avoid sourcing .sh file every time when one runs it, one may add the following to the `~/.bashrc`, where one needs to change .sh location and `WORKON_HOME` using location from $`echo $WORKON_HOME`. Sample format for the codes added to the ~/.bashrc is as follows:
```
export PATH="$PATH:/usr/local/bin/"
source /usr/local/bin/virtualenvwrapper.sh
export WORKON_HOME="$HOME/Envs" 
```
* Create virtual environment $`mkvirtualenv rango`. Run $`lsvirtualenv` to get the list of virtual environments, and run $`workon rango` to get in environment rango, for example.
* Run $`python --version` and $`python -c "import django; print(django.get_version())"` to check python version and django version.

# Django Basics
* Start the first project at work directory $`django-admin.py startproject tango_with_django_project`.
* Run $`python manage.py runserver` and $`python manage.py migrate` to start server and migrate the admin and apply migrations.
  * Run $`python manage.py runserver <your_machines_ip_address>:5555` to force the machine to run on specified port 5555.
* Create a new application, say, rango, using $`python manage.py startapp rango`.
* Go in the project folder and in the settings.py file, add the newly created app `rango` to the tuple `INSTALLED_APPS`.
* Create a sample view in the rango app:
  * Add a view function (on requst) called index in the `views.py` file
```python
from django.http import HttpResponse
def index(request):
  return HttpResponse("Rango says hey there world!")
```
* Add the rango app URL in the rango app folder's `urls.py` file (you may need to create this file). Basicall the following is to get the rango app url of the format `http://www.my_tango_django_project.com/rango/`
```python
from django.conf.urls import url
from rango import views
urlpatterns = [url(r'^$', views.index, name='index')]
```
  * To bring this url to the project urls, go to project's folder and add the following to the `urls.py` file. Then test it at url `http://127.0.0.1:8000/rango`
```python
from django.conf.urls import url, include
from rango import urls as rango_urls # this is from the rango app
# the following is added to the urlpatterns list
url(r'^$', 'rango.views.index_home', name='home') 
url(r'^rango/', include(rango_urls)) # ADD THIS NEW TUPLE to the list of the url patterns
```
* Create webpage templates for rango application.
  * Create folder `<workspace>/tango_with_django_project/templates/rango/`, then in the `tango_with_django_project` folder, add `TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)` to the `settings.py`, and also add `'DIRS': [os.path.join(BASE_DIR, 'templates')]` in the `TEMPLATES` dictionary in `settings.py`, where the `BASE_DIR` is already defined in the file by `BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))` (going two directories upward from the file settings.py to find the root workspace).

# Add Templates
* Add `index.html` file in rango app directory `templates/rango/` with following simple codes
```html
<!DOCTYPE html>
<html>

    <head>
        <title>Rango</title>
    </head>

    <body>
        <h1>Rango says...</h1>
        hello world! <strong>{{ boldmessage }}</strong><br />
        <a href="/rango/about/">About</a><br />
    </body>

</html>
```
* In `<workdir>/tango_with_django_project/rango/view.py` file, update index() function to call the {boldmessage} in the htlm code above.
```python
from django.shortcuts import render
def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context_dict)
```
* Create directory `<work directory>/tango_with_django_project/static/images/`. Store images and static media files here. In the `settings.py`, add the following static path information at the end.
```python
# add the template directory
print("Base Directory is " + BASE_DIR + "......")
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates/')
TEMPLATE_DIRS = (TEMPLATE_PATH,)
STATIC_PATH = os.path.join(BASE_DIR,'static')
STATIC_ROOT = ''
STATICFILES_DIRS = (
    STATIC_PATH,
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Absolute path to the media directory
```
* Add the loading of static media logo.png file in the images folder in `index.html`.
```html
<!DOCTYPE html>

{% load staticfiles %} <!-- This is for loading tag {% load static %}, where{% %} is the tag -->

<html>

    <head>
        <title>Rango</title>
    </head>

    <body>
        <h1>Rango says...</h1>
        hello world! <strong>{{ boldmessage }}</strong><br />
        <a href="/rango/about/">About</a><br />
        <img src="{% static "images/logo.png" %}" alt="Picture of Django" /> <!-- New line -->
    </body>

</html>

```
* Meanwhile, add the following to the `settings.py` to take care the case when DEBUG variable is set to False. In deployment stage, it should be set to False. In `urls.py` file of the project folder, add
```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
* In `models.py` under rango app directory, add following codes for creating the model that is essentially for webpage directory.
```python
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title

class UserProfile(models.Model):
    # A required line - links a UserProfile to User.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __unicode__(self):
        return self.user.username
```
* In `rango/admin.py`, add the page admin information for showing basic page information by adding
```python
from rango.models import Category, Page, UserProfile
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)
```
* Initiate first database by $`python manage.py migrate`, and create superuser $`python manage.py createsuperuser`. When there is a change to models, you need to register the change by running $`python manage.py makemigrations rango`.
* Add first item to the model, Category, through shells. Start shell by $`python manage.py shell` and add first item of Category named Test.
```python
# Import the Category model from the Rango application
from rango.models import Category
# Show all the current categories
print Category.objects.all()
# Create a new category object, and save it to the database.
c = Category(name="Test")
c.save()
# Now list all the category objects stored once more.
print Category.objects.all()
#[<Category: test>] # We now have a category called 'test' saved in the database!
# Quit the Django shell.
quit()
```
* User login
  * First, one needs to fix it by using `url(r'^admin/', include(admin.site.urls))` in the `urls.py` under project folder instead of using `admin/$`.
  * Make sure to run __makemigrations, migrate, etc__ to update the models once it's updated.
  * Create a dummy webpage using $`python populate_rango.py`, where .py file is created under the project folder `<workspace>/tango_with_django_project/` with following:
```python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
    python_cat = add_cat('Python')

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/")

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/")

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_cat("Django")

    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/")

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/")

    frame_cat = add_cat("Other Frameworks")

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/")

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org")

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
```
# Models, Templates, Views
* Add the model "Cateogry" to rango homepage. This will query database for model Cateogry. In `rango/views.py`, add
```python
from rango.models import Category
def index(request):
    category_list = Category.objects.order_by('-likes')[:5] # add top five categories of likes
    context_dict = {'boldmessage': "I am bold font from the context",
    			            	'categories': category_list}
    --------- Your Existing Code ---------
```
* In the `templates/rango/index.html` file, add the following to add top five categories (by likes) in the body part
```html
{% if categories %}
    <ul>
      {% for category in categories %}
      <li>{{ category.name }}</li>
      {% endfor %}
    </ul>
{% else %}
    <strong>There are no categories present.</strong>
{% endif %}
```
* Add Slug Field to deal with category table to deal with the urls with white space, e.g. www.abc.com/my table is converted to www.abc.com/my-table . In `rango/models.py`
```python
from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField()
    def save(self, *args, **kwargs):  # this is to override the parent class's save function
        #uncomment if you don't want the slug to change every time the name changes
        #if self.id is None:
            #self.slug=slugify(self.name)
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    #@property
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name
```
, then run $`python manage.py makemigrations rango` and $`python manage.py migrate` to update the rango models.
* In `rango/admin.py` file, update the category from the rango.models with the slug field.
```python
# Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)
```
* Create the category and page workflow
  * This is for creating links of category on homepage and it will direct to the pages with outside webpages. Basically this rango application is served as the web link directory.
  * In the `rango/views.py` file, import the Page definiton from rango.models you already defined and define tempalte for all categories.
```python
from rango.models import Page
def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)
```
  * Then in `<workspace>/tango_with_django_project/templates/rango/`, create the category.html file specifies above for each category webpage.
```python
<!DOCTYPE html>
<html>
    <head>
        <title>Rango</title>
    </head>

    <body>
        {% if category %}
        <h1>{{ category_name }}</h1>
            {% if pages %}
            <ul>
                {% for page in pages %}
                <li><a href="{{ page.url }}">{{ page.title }}</a></li>
                {% endfor %}
            </ul>
            {% else %}
                <strong>No pages currently in category.</strong>
            {% endif %}
        {% else %}
            The specified category {{ category_name }} does not exist!
        {% endif %}
    </body>
</html>
```
  * Update the `rango/urls.py` file by adding the category links to the urlpatterns
```python
urlpatterns = [url(r'^$', views.index, name='index'),
               #url(r'^about/$', views.about, name='about'),
               url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category')]
```
  * In the homepage for rango application, `<workspace>/tango_with_django+project/templates/rango/index.html`, add the following to the loop of category part, right under `{% for category in categories %}`
```html
<!-- Following line changed to add an HTML hyperlink -->
<li><a href="/rango/category/{{ category.slug }}">{{ category.name }}</a></li>
```
