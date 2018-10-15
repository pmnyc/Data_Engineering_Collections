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
* Forms
  * Create `ModelForm` class within the `rango/forms.py` file. The feature is to create "add category" or "add page" feature for the website and submit data into database.
```python
from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
        return cleaned_data
```
  * In the `rango/views.py`, add the add_cateogry feature for showing on the webpage to click.
```python
from rango.forms import CategoryForm
from rango.forms import PageForm


def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form': form, 'category': cat}
    return render(request, 'rango/add_page.html', context_dict)
```
  * Add the `add_category` webpage tempate for filling out forms. Create the `add_category.html` and `add_page.html` in the `templates/rango/` folder. Two html template codes are as follows:
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Rango</title>
    </head>

    <body>
        <h1>Add a Category</h1>

        <form id="category_form" method="post" action="/rango/add_category/">

            {% csrf_token %}
            {% for hidden in form.hidden_fields %}
                {{ hidden }}
            {% endfor %}

            {% for field in form.visible_fields %}
                {{ field.errors }}
                {{ field.help_text }}
                {{ field }}
            {% endfor %}

            <input type="submit" name="submit" value="Create Category" />
        </form>
    </body>

</html>
```

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Rango</title>
    </head>

    <body>
        <h1>Add a Page</h1>

        <form id="page_form" method="post" action="/rango/add_page/">

            {% csrf_token %}
            {% for hidden in form.hidden_fields %}
                {{ hidden }}
            {% endfor %}

            {% for field in form.visible_fields %}
                {{ field.errors }}
                {{ field.help_text }}
                {{ field }}
            {% endfor %}

            <input type="submit" name="submit" value="Create Page" />
        </form>
    </body>

</html>
```
  * Mapping the added features in the `views.py` through `rango/urls.py`. Add the following two items to the `urlpatterns` in the `urls.py` code.
```python
  url(r'^add_category/$', views.add_category, name='add_category'),
  url(r'^add_page/(?P<category_name_slug>[\w\-]+)$', views.add_page, name='add_page')
```
  * Add the links for adding the category and page (add-page link is in each category). In `templates/rango/index.html`, add the following code right before the `</body>` tag.
```html
<a href="/rango/add_category/">Add a New Category</a><br />
```
   * In the `templates/rango/category.html` file, add the following before the ending `</body>` tag.
```html
<a href="/rango/add_page/{{ category.slug }}">Add a New Page in {{category.name}}</a><br />
```
* User Authentification
  * In the `tango_with_django_project/settings.py` file, add the passworder hashers if one wants to use other encryption methods. Default one is PBKDF2PasswordHasher.
```python
PASSWORD_HASHERS = [
  'django.contrib.auth.hashers.PBKDF2PasswordHasher',
  'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]
```
  * Create UserProfile in the `rango/models.py` and specify the directory for storing pictures in the `media` folder. In `rango/admin.py` file, register UserProfile. Run $`python manage.py makemigrations rango` and $`python manage.py migrate` to make the changes to the models.py take effect. These are usually already included when launching the rango app at the beginning, so the details are skipped here. Try go through these files if one wants to repeat the same process of adding one feature in the models.py.
  * Creating the `UserForm` and `UserProfileForm` for users to fill out the user profile forms. In `rango/forms.py` file, add
```python
from django.contrib.auth.models import User
from rango.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
```
  * Creating the UserProfile register webpage in `rango/views.py`. 
```python
from rango.forms import UserForm, UserProfileForm

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'rango/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )
```
  * Creating the `rango/register.html` file.
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Rango</title>
    </head>

    <body>
        <h1>Register with Rango</h1>

        {% if registered %}
        Rango says: <strong>thank you for registering!</strong>
        <a href="/rango/">Return to the homepage.</a><br />
        {% else %}
        Rango says: <strong>register here!</strong><br />

        <form id="user_form" method="post" action="/rango/register/"
                enctype="multipart/form-data">

            {% csrf_token %}

            <!-- Display each form. The as_p method wraps each element in a paragraph
                 (<p>) element. This ensures each element appears on a new line,
                 making everything look neater. -->
            {{ user_form.as_p }}
            {{ profile_form.as_p }}

            <!-- Provide a button to click to submit the form. -->
            <input type="submit" name="submit" value="Register" />
        </form>
        {% endif %}
    </body>
</html>
```
  * Add the `url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!` line to the `urlpattern` list in the `rango/urls.py` file. Link them together by adding `<a href="/rango/register/">Register Here</a>` in the `templates/rango/index.html`.
  * Adding login and logout functionalities.
   * In `rango/views.py` file, add the functiosn for log-in and log-out.
```python
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'rango/login.html', {})

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

from django.contrib.auth import logout

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/rango/')
```

   * Create login template `templates/rango/login.html`.
```html
<!DOCTYPE html>
<html>
    <head>
        <!-- Is anyone getting tired of repeatedly entering the header over and over?? -->
        <title>Rango</title>
    </head>

    <body>
        <h1>Login to Rango</h1>

        <form id="login_form" method="post" action="/rango/login/">
            {% csrf_token %}
            Username: <input type="text" name="username" value="" size="50" />
            <br />
            Password: <input type="password" name="password" value="" size="50" />
            <br />

            <input type="submit" value="submit" />
        </form>

    </body>
</html>
```
   * Add urls `url(r'^login/$', views.user_login, name='login')`, `url(r'^login/$', views.user_login, name='login')` and `url(r'^login/$', views.user_login, name='login')` to the list of urlpatterns in `rango/urls.py`.
   * Add `LOGIN_URL = '/rango/login/'` in the `settings.py` so that the decorator `login_required()` will direct the users not logged in to the login webpage.
   * In the `templates/rango/index.html`, add the following code on the home page to show different login/logout and register features depending on the user login status.
```html
{% if user.is_authenticated %}
<a href="/rango/restricted/">Restricted Page</a><br />
<a href="/rango/logout/">Logout</a><br />
{% else %}
<a href="/rango/register/">Register Here</a><br />
<a href="/rango/login/">Login</a><br />
{% endif %}

<a href="/rango/about/">About</a><br/>
<a href="/rango/add_category/">Add a New Category</a><br />
```
# Working with Templates
* Abstracting a base html file `base.html` either in `templates` directory or `templates/rango/` directory depending on whether one wants to use this template in which app. In this case, we put `base.html` in the `templates/rango/` directory. Content of this `base.html` file is to abstract all basic webpage structures.
```html
<!DOCTYPE html>

<html>
    <head>
        <title>Rango - {% block title %}How to Tango with Django!{% endblock %}</title>
    </head>

    <body>
        <div>
            {% block body_block %}{% endblock %}
        </div>

        <hr />

        <div>
            <ul>
            {% if user.is_authenticated %}
                <li><a href="/rango/restricted/">Restricted Page</a></li>
                <li><a href="/rango/logout/">Logout</a></li>
                <li><a href="/rango/add_category/">Add a New Category</a></li>
            {% else %}
                <li><a href="/rango/register/">Register Here</a></li>
                <li><a href="/rango/login/">Login</a></li>
            {% endif %}

                <li><a href="/rango/about/">About</a></li>
            </ul>
        </div>
    </body>
</html>
```
* To inherite the template in `templates/rango/category.html`, we now can change the whole html file into the following code, assuming the base.html is in the `templates/rango` directory
```
{% extends 'rango/base.html' %}

{% load staticfiles %}

{% block title %}{{ category_name }}{% endblock %}

{% block body_block %}
    <h1>{{ category_name }}</h1>
    {% if category %}
        {% if pages %}
        <ul>
                {% for page in pages %}
                <li><a href="{{ page.url }}">{{ page.title }}</a></li>
                {% endfor %}
                </ul>
        {% else %}
                <strong>No pages currently in category.</strong>
        {% endif %}

                {% if user.is_authenticated %}
                <a href="/rango/add_page/{{ category.slug }}">Add a New Page in {{category.name}}</a><br />
                {% endif %}
        {% else %}
                 The specified category {{ category_name }} does not exist!
    {% endif %}

{% endblock %}
```
* Changing the url style in a more modern way. In `index.html`, we may change the link to the category webpage from `<li><a href="/rango/category/{{ category.slug }}">{{ category.name }}</a></li>` to `<li><a href="{% url 'category'  category.slug %}">{{ category.name }}</a></li>`. The new style finds the urls.py file and locates the name specified in the new href style (see below). We can also change the url styles in `templates/rango/base.html` to
```html
<div>
        <ul>
    {% if user.is_authenticated %}
        <li><a href="{% url 'restricted' %}">Restricted Page</a></li>
        <li><a href="{% url 'logout' %}">Logout</a></li>
        <li><a href="{% url 'add_category' %}">Add a New Category</a></li>
    {% else %}
        <li><a href="{% url 'register' %}">Register Here</a></li>
        <li><a href="{% url 'login' %}">Login</a></li>
    {% endif %}

    <li><a href="{% url 'about' %}">About</a></li>
    </ul>
</div>
```
# Cookies and Sessions
* Update index() function in `rango/views.py`. Two functions below are for saving cookies on clinet side making cookies expire after browser is closed, and the other method of saving cookies on server side.
```python
from datetime import datetime

def index(request):
    ## This is to get visits through the reqeust sessions stored on server side
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {'categories': category_list, 'pages': page_list}

    visits = request.session.get('visits')
    if not visits:
        visits = 1
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_visit_time).seconds > 0:
            # ...reassign the value of the cookie to +1 of what it was before...
            visits = visits + 1
            # ...and update the last visit cookie, too.
            reset_last_visit_time = True
    else:
        # Cookie last_visit doesn't exist, so create it to the current date/time.
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits
    context_dict['visits'] = visits


    response = render(request,'rango/index.html', context_dict)

    return response
```

```python
from datetime import datetime

def index(request):
    ## this is to get the cookies saved on client side
    category_list = Category.objects.all()
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}

    # Get the number of visits to the site.
    # We use the COOKIES.get() function to obtain the visits cookie.
    # If the cookie exists, the value returned is casted to an integer.
    # If the cookie doesn't exist, we default to zero and cast that.
    visits = int(request.COOKIES.get('visits', '1'))

    reset_last_visit_time = False
    response = render(request, 'rango/index.html', context_dict)
    # Does the cookie last_visit exist?
    if 'last_visit' in request.COOKIES:
        # Yes it does! Get the cookie's value.
        last_visit = request.COOKIES['last_visit']
        # Cast the value to a Python date/time object.
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        # If it's been more than a day since the last visit...
        if (datetime.now() - last_visit_time).days > 0:
            visits = visits + 1
            # ...and flag that the cookie last visit needs to be updated
            reset_last_visit_time = True
    else:
        # Cookie last_visit doesn't exist, so flag that it should be set.
        reset_last_visit_time = True

        context_dict['visits'] = visits

        #Obtain our Response object early so we can add cookie information.
        response = render(request, 'rango/index.html', context_dict)

    if reset_last_visit_time:
        response.set_cookie('last_visit', datetime.now())
        response.set_cookie('visits', visits)

    # Return response back to the user, updating any cookies that need changed.
    return response
```
* Browser-Length and Persistent Sessions for two weeks to expire. In `settings.py`, put `SESSION_EXPIRE_AT_BROWSER_CLOSE = True` or `SESSION_EXPIRE_AT_BROWSER_CLOSE = False` and `SESSION_COOKIE_AGE=1209600` in.
* To clear the cookies stored in sessions when they accumulate, run $`python manage.py clearsessions`.

# User Authentication with Django-Registration-Redux
* In `settings.py` file, add `'registration', # add in the registration package` to the tuple `INSTALLED_APPS`. Meanwhile, add
```python
REGISTRATION_OPEN = True                # If True, users can register
ACCOUNT_ACTIVATION_DAYS = 7     # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True  # If True, the user will be automatically logged in.
LOGIN_REDIRECT_URL = '/rango/'  # The page you want users to arrive at after they successful log in
LOGIN_URL = '/accounts/login/'  # The page users are directed to if they are not logged in,
                                                                # and are trying to access pages requiring authentication
```
* In `tango_with_django_project/urls.py` file, add `url(r'^accounts/', include('registration.backends.simple.urls')),` to the tuple `urlpatterns`. The Django Registration Redux package provides the machinery for numerous functions such as two-step registration, password change, etc.
* In the `templates/registration` directory, create `login.html` with
```html
{% extends "rango/base.html" %}

{% block body_block %}
<h1>Login</h1>
        <form method="post" action=".">
                {% csrf_token %}
                {{ form.as_p }}

                <input type="submit" value="Log in" />
                <input type="hidden" name="next" value="{{ next }}" />
                </form>

        <p>Not  a member? <a href="{% url 'registration_register' %}">Register</a>!</p>
{% endblock %}
```
* Continue above. Create `registration_form.html` with
```html
{% extends "rango/base.html" %}


{% block body_block %}
<h1>Register Here</h1>
        <form method="post" action=".">
                {% csrf_token %}
                {{ form.as_p }}

                <input type="submit" value="Submit" />
        </form>
{% endblock %}
```
* Continue above. Create `registration_complete.html` with
```html
{% extends "rango/base.html" %}


{% block body_block %}
<h1>Registration Complete</h1>
        <p>You are now registered</p>
{% endblock %}
```
* Continue above. Create `logout.html` with the following code and then check the result from [`http://127.0.0.1:8000/accounts/register/`] (http://127.0.0.1:8000/accounts/register/)
```html
{% extends "rango/base.html" %}


{% block body_block %}
<h1>Logged Out</h1>
        <p>You are now logged out.</p>
{% endblock %}
```
* In `templates\rango\base.html` file, try to update the corresponding href part with the following
  * Update register to point to `<a href="{% url 'registration_register' %}">`
  * login to point to `<a href="{% url 'auth_login' %}">`, and
  * logout to point to `<a href="{% url 'auth_logout' %}?next=/rango/">`, where the `?next=` is just to direct the webpage the rango home page.
  * In `settings.py`, update LOGIN_URL to be `'/accounts/login/'`.
* To modify the registration flow (such as where to exit after the login logout, etc.), add the following code for redirecting the webpage after login.
```python
from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/rango/'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
        #Add in this url pattern to override the default pattern in accounts.
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
```
# Bootstrapping Rango using the Twitter Bootstrap 3.2 toolkit. Here are some [example layouts](http://getbootstrap.com/getting-started/#examples) and [dashboard styles](http://getbootstrap.com/examples/dashboard/). 
* Use twitter boostrap to create new `templates/rango/base.html`.
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="http://getbootstrap.com/favicon.ico">

    <title>Rango - {% block title %}How to Tango with Django!{% endblock %}</title>

    <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="http://getbootstrap.com/examples/dashboard/dashboard.css" rel="stylesheet">

    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/rango/">Rango</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav navbar-right">
                <li><a href="{% url 'index' %}">Home</a></li>
                    {% if user.is_authenticated %}
                        <li><a href="{% url 'restricted' %}">Restricted Page</a></li>
                        <li><a href="{% url 'auth_logout' %}?next=/rango/">Logout</a></li>
                        <li><a href="{% url 'add_category' %}">Add a New Category</a></li>
                    {% else %}
                        <li><a href="{% url 'registration_register' %}">Register Here</a></li>
                        <li><a href="{% url 'auth_login' %}">Login</a></li>
                    {% endif %}
                                <li><a href="{% url 'about' %}">About</a></li>

              </ul>
        </div>
      </div>
    </div>

    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">
                {% block side_block %}{% endblock %}

        </div>
        <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
           <div>
                {% block body_block %}{% endblock %}
                </div>
        </div>
      </div>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="http://getbootstrap.com/dist/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="http://getbootstrap.com/assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
```
* Update `templates/rango/about.html` with
```html
{% extends 'rango/base.html' %}

{% load staticfiles %}

{% block title %}About{% endblock %}

{% block body_block %}
    <div class="page-header">
                <h1>About</h1>
            </div>
            <div>
            <p></strong>.</p>

            <img  width="90" height="100" src="{% static "images/rango.jpg" %}" alt="Picture of Rango" /> <!-- New line -->
            </div>
{% endblock %}
```
* Update `templates/rango/index.html` with
```html
{% extends 'rango/base.html' %}

{% load staticfiles %}

{% block title %}Index{% endblock %}

        {% block body_block %}
{% if user.is_authenticated %}
    <div class="page-header">

                <h1>Rango says... hello {{ user.username }}!</h1>
            {% else %}
                <h1>Rango says... hello world!</h1>
            {% endif %}
</div>

         <div class="row-fluid">

                     <div class="span6">
               <div class="panel panel-primary">
    <div class="panel-heading">
            <h3 class="panel-title">Top Five Categories</h3>
    </div>
</div>

              {% if categories %}
                    <ul>
                        {% for category in categories %}
                         <li><a href="{% url 'category'  category.slug %}">{{ category.name }}</a></li>
                        {% endfor %}
                    </ul>
                {% else %}
                    <strong>There are no categories present.</strong>
                {% endif %}

            </div>
            <div class="span6">
              <div class="panel panel-primary">
            <div class="panel-heading">
                    <h3 class="panel-title">Pages</h3>
            </div>
    </div>

                {% if pages %}
                    <ul>
                        {% for page in pages %}
                         <li><a href="{{page.url}}">{{ page.title }}</a></li>
                        {% endfor %}
                    </ul>
                {% else %}
                    <strong>There are no categories present.</strong>
                {% endif %}
            </div>

          </div>


       <p> visits: {{ visits }}</p>
        {% endblock %}
```
* Udpate `templates/rango/login.html` with
```html
{% extends "rango/base.html" %}

{% block body_block %}
<link href="http://getbootstrap.com/examples/signin/signin.css" rel="stylesheet">

<form class="form-signin" role="form" method="post" action=".">
{% csrf_token %}

<h2 class="form-signin-heading">Please sign in</h2>
<input class="form-control" placeholder="Username" id="id_username" maxlength="254" name="username" type="text" required autofocus=""/>
<input type="password" class="form-control" placeholder="Password" id="id_password" name="password"  required />

        <button class="btn btn-lg btn-primary btn-block" type="submit" value="Submit" >Sign in</button>
        </form>

{% endblock %}
```
* Update `templates/rango/add_page.html` with
```html
{% extends 'rango/base.html' %}

{% block title %}Add Page{% endblock %}


{% block body_block %}
{% if category %}

                <form role="form"  id="page_form" method="post" action="/rango/category/{{category.slug}}/add_page/">
            <h2 class="form-signin-heading">Add a Page to <a href="/rango/category/{{category.slug}}/"> {{ category.name }}</a></h2>
                    {% csrf_token %}
                    {% for hidden in form.hidden_fields %}
                        {{ hidden }}
                    {% endfor %}

                    {% for field in form.visible_fields %}
                        {{ field.errors }}
                        {{ field.help_text }}<br/>
                        {{ field }}<br/>
                    {% endfor %}

                <br/>
            <button class="btn btn-primary" type="submit" name="submit">Add Page</button>
                </form>
            {%  else %}
            <p>This is category does not exist.</p>
        {%  endif %}


        {% endblock %}
```
* Update `templates/rango/registration_form.html` with
```html
{% extends 'rango/base.html' %}

{% block title %}Add Page{% endblock %}


{% block body_block %}
{% if category %}

                <form role="form"  id="page_form" method="post" action="/rango/category/{{category.slug}}/add_page/">
            <h2 class="form-signin-heading">Add a Page to <a href="/rango/category/{{category.slug}}/"> {{ category.name }}</a></h2>
                    {% csrf_token %}
                    {% for hidden in form.hidden_fields %}
                        {{ hidden }}
                    {% endfor %}

                    {% for field in form.visible_fields %}
                        {{ field.errors }}
                        {{ field.help_text }}<br/>
                        {{ field }}<br/>
                    {% endfor %}

                <br/>
            <button class="btn btn-primary" type="submit" name="submit">Add Page</button>
                </form>
            {%  else %}
            <p>This is category does not exist.</p>
        {%  endif %}


        {% endblock %}
```
# Template Tags
* Add cateogries on the side bar for each page so that customers can browse while on one page. Create directory `rango/templatetags` and files `__init__.py` and `rango_extras.py`. Here is sample code for `rango_extras.py` that can include the tags.
```python
from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(), 'act_cat': cat}
```
* Create template file for showing categories `templates/rango/cats.html`. Here is the code for for the cats.html.
```html
{% if cats %}
    <ul class="nav nav-sidebar">
    {% for c in cats %}
        {% if c == act_cat %} <li  class="active" > {% else  %} <li>{% endif %}
            <a href="{% url 'category'  c.slug %}">{{ c.name }}</a></li>
    {% endfor %}

{% else %}
    <li> <strong >There are no category present.</strong></li>

    </ul>
{% endif %}
```
* Also update the `templates/rango/base.html` to add the categrories to the side bar.
```html
<!DOCTYPE html>
{% load static %}
{% load rango_extras %}

... all other componenets remain intact ...

<div class="col-sm-3 col-md-2 sidebar">
                {% block side_block %}
                {% get_category_list category%}
                {% endblock %}

        </div>
```
# Adding External Search Functionality
* Add Bing Search API. Create `bing_search.py` under rango application directory, and update this file with code
```python
import json
import urllib, urllib2

# Add your BING_API_KEY

BING_API_KEY = '<insert_bing_api_key>'

def run_query(search_terms):
    # Specify the base
    root_url = 'https://api.datamarket.azure.com/Bing/Search/'
    source = 'Web'

    # Specify how many results we wish to be returned per page.
    # Offset specifies where in the results list to start from.
    # With results_per_page = 10 and offset = 11, this would start from page 2.
    results_per_page = 10
    offset = 0

    # Wrap quotes around our query terms as required by the Bing API.
    # The query we will then use is stored within variable query.
    query = "'{0}'".format(search_terms)
    query = urllib.quote(query)

    # Construct the latter part of our request's URL.
    # Sets the format of the response to JSON and sets other properties.
    search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
        root_url,
        source,
        results_per_page,
        offset,
        query)

    # Setup authentication with the Bing servers.
    # The username MUST be a blank string, and put in your API key!
    username = ''


    # Create a 'password manager' which handles authentication for us.
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, search_url, username, BING_API_KEY)

    # Create our results list which we'll populate.
    results = []

    try:
        # Prepare for connecting to Bing's servers.
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)

        # Connect to the server and read the response generated.
        response = urllib2.urlopen(search_url).read()

        # Convert the string response to a Python dictionary object.
        json_response = json.loads(response)

        # Loop through each page returned, populating out results list.
        for result in json_response['d']['results']:
            results.append({
            'title': result['Title'],
            'link': result['Url'],
            'summary': result['Description']})

    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError as e:
        print "Error when querying the Bing API: ", e

    # Return the list of results to the calling function.
    return results

```
* One may create a file for storing the API keys, passwords, etc. in a file that is not included in the github repository. Now we may need to create the `templates/rango/search.html` file for doing Bing search.
```html
{% extends "rango/base.html" %}

{% load staticfiles %}

{% block title %}Search{% endblock %}

{% block body_block %}

    <div class="page-header">
        <h1>Search with Rango</h1>
    </div>

    <div class="row">

        <div class="panel panel-primary">
            <br/>

            <form class="form-inline" id="user_form" method="post" action="{% url 'search' %}">
                {% csrf_token %}
                <!-- Display the search form elements here -->
                <input class="form-control" type="text" size="50" name="query" value="" id="query" />
                <input class="btn btn-primary" type="submit" name="submit" value="Search" />
                <br />
            </form>

            <div class="panel">
                {% if result_list %}
                    <div class="panel-heading">
                    <h3 class="panel-title">Results</h3>
                    <!-- Display search results in an ordered list -->
                    <div class="panel-body">
                        <div class="list-group">
                            {% for result in result_list %}
                                <div class="list-group-item">
                                    <h4 class="list-group-item-heading"><a href="{{ result.link }}">{{ result.title }}</a></h4>
                                    <p class="list-group-item-text">{{ result.summary }}</p>
                                </div>
                            {% endfor %}
                        </div>
                    </div>
                {% endif %}
                </div>
            </div>
 </div>

{% endblock %}
```
* After adding new template, we need to update `rango/view.py` so that `http://.../rango/search` on address can link to the `search.html`.
```python
from rango.bing_search import run_query

def search(request):
    result_list = []
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)
    return render(request, 'rango/search.html', {'result_list': result_list})
```
* Update `rango/urls.py` for the url address pattern. Add `url(r'^search/$', views.search, name='search')` to the list of `urlpatterns` in the code.
* Add Bing Search on the top of the bar. Add the following codes to the corresponding navigation bar (search for `<ul class="nav navbar-nav navbar-right">`) in the code `templates/rango/base.html`
```html
<ul class="nav navbar-nav navbar-right">
              <li><a href="{% url 'search' %}">Bing Search</a></li>
```

# Making Rango Tango! Exercises
* Track Page Click Throughs. Add the track url functionality through `rango/views.py`
```python
from django.shortcuts import redirect

def track_url(request):
    context = RequestContext(request)
    page_id = None
    url = '/rango/'
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
            try:
                page = Page.objects.get(id=page_id)
                page.views = page.views + 1
                page.save()
                url = page.url
            except:
                pass
    return redirect(url)
```
  * Update the mapping from url to view functionality in file `rango/urls.py` by adding `url(r'^goto/$', views.track_url, name='track_url'),` to the list `urlpatterns`.
  * Add the code for changing the page link using page.id instead of direct or original url of page. Search for `{% for page in pages %} {% endfor %}` in `templates/rango/category.html` and add the following code
```html
                <li>
                <a href="/rango/goto/?page_id={{page.id}}">{{page.title}}</a>
                {% if page.views > 1 %}
                    - ({{ page.views }} views)
                {% elif page.views == 1 %}
                    - ({{ page.views }} view)
                {% endif %}
                </li>
```
* Create a search form on each category webpage. In `templates/rango/category.html`, add the following code in the body part for adding search form.
```html
    <div class="hero-unit">
	<div class="container-fluid">
	    <p>Search for a page.</p>
		 <form class="form-inline" id="user_form" method="post" action="{% url 'category'  category.slug %}">
             {% csrf_token %}
             <!-- Display the search form elements here -->
             <input class="form-control" type="text" size="50" name="query" value="{{query}}" id="query" />
             <input class="btn btn-primary" type="submit" name="submit" value="Search" />
         </form>
	</div>

	<div class="container-fluid">
		{% if result_list %}
			<!-- Display search results in an ordered list -->
			<ol>
				{% for result in result_list %}
				<li>
                    {% if user.is_authenticated %}
		    <button data-catid="{{category.id}}" data-title="{{ result.title }}" data-url="{{ result.link }}" class="rango-add btn btn-mini btn-info" type="button">Add</button>
	        {% endif %}
					<strong><a href="{{ result.link }}">{{ result.title }}</a></strong><br />
					<p>{{ result.summary }}</p>
				</li>
				{% endfor %}
			</ol>
		{% else %}
			<br/>
			<p>No results found</p>
		{% endif %}
	</div>
    </div>
```
* Update the function category in `rango/views.py` so that it can add the result_list through search API in the context.
```python
def category(request, category_name_slug):
    context_dict = {}
    context_dict['result_list'] = None
    context_dict['query'] = None
    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)

            context_dict['result_list'] = result_list
            context_dict['query'] = query

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category).order_by('-views')
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    if not context_dict['query']:
        context_dict['query'] = category.name

    return render(request, 'rango/category.html', context_dict)
```

# JQuery and Django
* JQuery provides a suite of functionality that is mainly focused on manipulating HTML elements. First, include JQuery in your Django Project/Application. In the 'templates/rango/base.html' file, add the js scripts to load before the end of the body. One may either use the abosoute path from other websites or download js scripts in the js folder stored in the `tango_with_django_project/static/js` folder.
```html
<!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="http://getbootstrap.com/dist/js/bootstrap.min.js"></script>
    <script src="{% static 'js/rango-jquery.js' %}"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="http://getbootstrap.com/assets/js/ie10-viewport-bug-workaround.js"></script>
```
* Each JQuery javascript file within js folder starts with
```javascript
$(document).ready(function() {
        // JQuery code to be added in here.
});
```
* Test some jQuery js script by adding the following codes to the `templates/rango/about.html` in the body block. Where the `<p>` is an HTML tag, which will be searched in a js selector in `static/js/rango-jquery.js` for changing colors when mouse is hovering on it or not. The other two added below are two buttons for displaying some alert message after the click and adding o the word "Hello" on about webpage when word "Hello" is labeled by id="msg", which is searched in the `static/js/rango-jquery.js` java script.
```html
    <div id="msg">Hello</div>

    <button onClick="alert('You clicked the button using Javascript.');">
       Click Me - I run Javascript
    </button>

    <button id="about-btn"> Click Me - I'm Javascript on Speed</button>
    <p>This is a example</p>
    <p>This is another example</p>
```
* DOM Manipulation Example. In the `static/js/rango-jquery.js` file, we add the following function for performing warnings, adding "o" to the world labled by ID #msg, changing word colors when mouse is hovering on it, searching for class "ouch" and display alert after the link is clicked.
```javascript
$(document).ready( function() {

    $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
    });

    $(".ouch").click( function(event) {
        alert("You clicked me! ouch!");
    });

    $("p").hover( function() {
            $(this).css('color', 'red');
    },
    function() {
            $(this).css('color', 'blue');
    });

    $("#about-btn").click( function(event) {
        msgstr = $("#msg").html()
        msgstr = msgstr + "o"
        $("#msg").html(msgstr)
         });
});
```
# AJAX in Django with JQuery
* Add JavaScript location near the end of the `templates/rango/base.html` file for loading the javascript when the base page is called. If static is specified, put the corresponding .js file in the directory `rango_demo/tango_with_django_project/static/js`
```html
<script src="{% static "js/jquery.js" %}"></script>
<script src="{% static "js/rango-ajax.js" %}"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="http://getbootstrap.com/dist/js/bootstrap.min.js"></script>
```
* Add "Like" thumbs up button to the category pages through `tango_with_django_project/templates/rango/category.html`. Below the commented part is for showing like button only when user loggs in.
```html
<div>
    <p>
    <strong id="like_count">{{ category.likes }}</strong> people like this category
    <!-- 
    {% if user.is_authenticated %}
            <button id="likes" data-catid="{{category.id}}" class="btn btn-primary" type="button">
            <span class="glyphicon glyphicon-thumbs-up"></span>
            Like
            </button>
    {% endif %}
    -->
    <button id="likes" data-catid="{{category.id}}" class="btn btn-primary" type="button">
    <span class="glyphicon glyphicon-thumbs-up"></span>
    Like
    </button>
    </p>
</div>
```
* Add `like_category` view function to `tango_with_django_project/rango/views.py` to create a Like Category View.
```python
django.contrib.auth.decorators import login_required

@login_required
def like_category(request):

    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id'] # category_id is given here assuming user is on that certain category

    likes = 0
    if cat_id:
        cat = Category.objects.get(id=int(cat_id))
        if cat:
            likes = cat.likes + 1
            cat.likes =  likes
            cat.save()

    return HttpResponse(likes)
```
* Add the `like_category` category to the `tango_with_django_project/rango/urls.py` file to update the url pattern.
```python
url(r'^like_category/$', views.like_category, name='like_category')
```
* To make the AJAX request by adding the following code to `rango-ajax.js`. When Like button (represented by #likes) is clicked, it will call the `like_category` function in the view.py and return the result to id `like_count` specified in the `category.html` template. Once the user clicks on like, the like button will be hidden/dissapear.
```javascript
$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/rango/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});
```
* Parameterise the Get Category list function by, say, listing top 8 cateogries that start with given suggestion. Add the following code to `tango_with_django_project/rango/views.py`.
```python

def get_category_list(max_results=0, starts_with=''):
        cat_list = []
        if starts_with:
                cat_list = Category.objects.filter(name__istartswith=starts_with)

        if max_results > 0:
                if cat_list.count() > max_results:
                        cat_list = cat_list[:max_results]

        return cat_list

def suggest_category(request):
        cat_list = []
        starts_with = ''
        if request.method == 'GET':
                starts_with = request.GET['suggestion']

        cat_list = get_category_list(8, starts_with)

        return render(request, 'rango/category_list.html', {'cat_list': cat_list })
```
* Update the urls pattern in the file `rango_demo/tango_with_django_project/rango/urls.py` after adding the functions to views.py
```python
url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
```
* Update the suggestion and filter features above to display through the base template in the sidebar div in <body> part of the file `tango_with_django_project/templates/rango/base.html`. First three lines below are just for locating the part for putting the code in, don't add these top 3 lines below to the file. We have added in an input box with id="suggestion" and div with id="cats" in which we will display the response.
```html
<div class="container-fluid">
  <div class="row">
    <div class="col-sm-3 col-md-2 sidebar">


<ul class="nav nav-list">
        <li class="nav-header">Find a Category</li>
        <form>
        <label></label>
        <li><input  class="search-query span10" type="text" name="suggestion" value="" id="suggestion" /></li>
        </form>
</ul>

<div id="cats">
</div>
```
* Update the file `tango_with_django_project/static/js/rango-ajax.js` file by returning the suggest category(s) when class id=suggestion (refers to #suggestion below) filter is called in above suggestion search box.
```javascript
$('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/rango/suggest_category/', {suggestion: query}, function(data){
         $('#cats').html(data);
        });
});
```
# Run Test
* Running tests through command line $`python manage.py test rango`.
* Create the `rango/tests.py` file by adding the following testcase to see if negative views can pass. Then run $`python manage.py test rango` to test.
```python
from django.test import TestCase
from rango.models import Category

class CategoryMethodTests(TestCase):

    def test_ensure_views_are_positive(self):
        """
                ensure_views_are_positive should results True for categories where views are zero or positive
        """
                cat = Category(name='test',views=-1, likes=0)
                cat.save()
                self.assertEqual((cat.views >= 0), True) #See the Python Documentation on unit tests, https://docs.python.org/2/library/unittest.html for other commands (i.e. assertItemsEqual, assertListEqual, assertDictEqual, etc)
                
     def test_slug_line_creation(self):
             """
             slug_line_creation checks to make sure that when we add a category an appropriate slug line is created
             i.e. "Random Category String" -> "random-category-string"
             """

             cat = Category('Random Category String')
             cat.save()
             self.assertEqual(cat.slug, 'random-category-string')
```
* Let’s create a test that checks that when the index page loads, it displays the message that There are no categories present, when the Category model is empty. Codes are stored in `rango/tests.py`. It does this with a mock client, that internally calls a django view via the url. The django TestCase has access to a client object, which can make requests. Here, it uses the helper function reverse to look up the url of the index page. Then it tries to get that page, where the response is stored. The test then checks a number of things: did the page load ok? Does the response, i.e. the html contain the phrase “There are no categories present.”, etc.
```python
from django.core.urlresolvers import reverse

class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])

from rango.models import Category

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
return c

def test_index_view_with_categories(self):
    """
    If no questions exist, an appropriate message should be displayed.
    """

    add_cat('test',1,1)
    add_cat('temp',1,1)
    add_cat('tmp',1,1)
    add_cat('tmp test temp',1,1)

    response = self.client.get(reverse('index'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "tmp test temp")

    num_cats =len(response.context['categories'])
    self.assertEqual(num_cats , 4)
```
* Coverage Testing measures how much of your code base has been tested, and how much of your code has been put through its paces via tests. You can install a package called coverage via with pip install coverage which automatically analyses how much code coverage you have. Once you have coverage installed, run the following command: $`coverage run --source='.' manage.py test rango`

# Deploying Your Project
* To load up the rango environment, use $`workon rango`. Run $`deactivate` to leave the current environment.
* After git clone the repository, run the following commands to start. $`python manage.py makemigrations rango` , $`python manage.py migrate` , $`python populate_rango.py` , $`python manage.py createsuperuser`
