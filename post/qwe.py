a = {
    '_validators': [],
    'allow_null': False,
    '_args': "(<User: djon>,)",
    'initial': None,
    '_creation_counter': 3,
    'write_only': False,
    'instance': "<User: djon>",
    'help_text': None,
    '_kwargs': {},
    'source': None,
    'required': True,
    '_fields': {
        'last_name': CharField(
            allow_blank=True,
            max_length=150,
            required=False
        ),
        'is_active': BooleanField(
            help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
            label='Active', required=False
        ),
        'date_joined': DateTimeField(required=False),
        'is_staff': BooleanField(
            help_text='Designates whether the user can log into this admin site.',
            label='Staff status', required=False
        ),
        'id': IntegerField(label='ID', read_only=True),
        'username': CharField(
            help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
            max_length=150,
            validators=[]
        ),
        'email': EmailField(
            allow_blank=True,
            label='Email address',
            max_length=254,
            required=False
        ),
        'url': HyperlinkedIdentityField(view_name='user-detail'),
        'first_name': CharField(
            allow_blank=True,
            max_length=30,
            required=False
        )
    },
    '_readable_fields': [
        HyperlinkedIdentityField(view_name='user-detail'),
        IntegerField(label='ID', read_only=True),
        CharField(
            help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
            max_length=150,
            validators=[
                "<django.contrib.auth.validators.UnicodeUsernameValidator object>",
                "<UniqueValidator(queryset=User.objects.all())>"
            ]
        ),
        CharField(allow_blank=True, max_length=30, required=False),
        CharField(allow_blank=True, max_length=150, required=False),
        EmailField(
            allow_blank=True,
            label='Email address',
            max_length=254,
            required=False
        ),
        BooleanField(
            help_text='Designates whether the user can log into this admin site.',
            label='Staff status',
            required=False
        ),
        BooleanField(
            help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
            label='Active',
            required=False
        ),
        DateTimeField(required=False)
    ],
    'label': None,
    '_writable_fields': [
        CharField(
            help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
            max_length=150,
            validators=[
                "<django.contrib.auth.validators.UnicodeUsernameValidator object>",
                "<UniqueValidator(queryset=User.objects.all())>"
            ]
        ),
        CharField(
            allow_blank=True,
            max_length=30,
            required=False
        ),
        CharField(
            allow_blank=True,
            max_length=150,
            required=False
        ),
        EmailField(
            allow_blank=True,
            label='Email address',
            max_length=254,
            required=False
        ),
        BooleanField(
            help_text='Designates whether the user can log into this admin site.',
            label='Staff status',
            required=False
        ),
        BooleanField(
            help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
            label='Active',
            required=False
        ),
        DateTimeField(required=False)
    ],
    'style': {},
    'url_field_name': 'url',
    'parent': None,
    'field_name': None,
    'error_messages': {
        'invalid': 'Invalid data. Expected a dictionary, but got {datatype}.',
        'required': 'This field is required.',
        'null': 'This field may not be null.'
    },
    '_context': {},
    'read_only': False,
    'default': "<class 'rest_framework.fields.empty'>",
    'partial': False
}


for i in a:
    print(i, ":::", a[i])
