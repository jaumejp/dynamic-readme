# Libraries
import random

# Custom modules
from helpers.config import COLOR_NAME, RANDOM_TAGS, MSG_WIDTH, YOUR_NAME, YOUR_ROLE, YOUR_COMPANY, YOUR_LOCATION
from helpers.functions import get_temp_max_from, get_current_day_name, shuffle_dictionary

# SVG tag variables
TAG_PADDING = 10
TAG_HEIGHT = 25
IMG_HEIGHT = 220

# SVG template variables
IMG_WIDTH = 200
MSG_PADDING_X = 15

SVG_TAG_WIDTH = MSG_WIDTH +IMG_WIDTH +MSG_PADDING_X

# Custom information variables
temperature = get_temp_max_from(YOUR_LOCATION) or '19.9'

ES_DAYS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
EN_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Language variables
LANGUAGES = {
    0: {
        'lang': 'es',
        'traductions': {
            'msg_1': f"Hola soy {YOUR_NAME}. Contactame en LinkedIn",
            'msg_2': f"Soy {YOUR_ROLE} en {YOUR_COMPANY}",
            'msg_3': f"Soy de {YOUR_LOCATION} y hoy tenemos {temperature}°C",
            'msg_4': f"Que tengas un buen {get_current_day_name(ES_DAYS)} 👋",
        }
    },

    1: {
        'lang': 'en',
        'traductions': {
            'msg_1': f"I'm {YOUR_NAME}. Contact me on LinkedIn",
            'msg_2': f"I'm a {YOUR_ROLE} at {YOUR_COMPANY}",
            'msg_3': f"I'm from {YOUR_LOCATION} and today it's {temperature}°C",
            'msg_4': f"Have a great {get_current_day_name(EN_DAYS)} 👋",
        }
    },

    # 2: {
    #     'lang': '---',
    #     'traductions': {
    #         'msg_1': "---",
    #         'msg_2': "---",
    #         'msg_3': "---",
    #         'days_of_week': ["", "", "", "", "", "", ""],
    #         'msg_4': "---",
    #     }
    # }
}

# Color variables
COLORS = {
    'red': {'primary': '#D71013', 'secondary': '#FEF2F2'},
    'green': {'primary': '#09824F', 'secondary': '#ECFDF5'},
    'darkred': {'primary': '#AB0D04', 'secondary': '#FEF4F3'},
    'blue': {'primary': '#003E84', 'secondary': '#FCFFFA'},
    'lightblue': {'primary': '#3D93AC', 'secondary': '#EBFFFE'},
    'purple': {'primary': '#5402D0', 'secondary': '#F5E7FF'},
    'lime': {'primary': '#456416', 'secondary': '#F1FBE2'},
    'brown': {'primary': '#9E5E09', 'secondary': '#FFFBE8'},
    'gray': {'primary': '#27364B', 'secondary': '#F9FAFD'},
    'orange': {'primary': '#f7b411', 'secondary': '#fffbf2'},
    'magenta': {'primary': '#f56767', 'secondary': '#f7e6e6'},
    'pink': {'primary': '#fc17ef', 'secondary': '#f7e6f6'},
}

color = random.choice(list(COLORS.keys())) if COLOR_NAME is None else COLOR_NAME

# Tag categories variables
CATEGORIES = {
    1: ('Programming Languages', 'gray'),
    2: ('JavaScript Frameworks', 'brown'),
    3: ('Backend Frameworks', 'green'),
    4: ('Frontend Technologies', 'purple'),
    5: ('Databases', 'lime'),
    6: ('DevOps and CI/CD Tools', 'blue'),
    7: ('Version Control', 'darkred'),
    8: ('Cloud Services', 'lightblue'),
    9: ('Collaboration and Project Management Tools', 'red'),
    10: ('Containers and Virtualization', 'orange'),
    11: ('Operating Systems', 'magenta'),
    12: ('Others', 'pink'),
}

TECHNOLOGIES = {
    # Programming Languages
    'JavaScript': {'category': 1, 'width': 80},
    'Python': {'category': 1, 'width': 67},
    'Java': {'category': 1, 'width': 55},
    # 'C#': { 'category': 1, 'width': 45},
    # 'C++': {'category': 1, 'width': 53},
    # 'Ruby': {'category': 1, 'width': 57},
    # 'Go': {'category': 1, 'width': 45},
    # 'Swift': {'category': 1, 'width': 58},
    # 'Kotlin': {'category': 1, 'width': 60},
    'PHP': {'category': 1, 'width': 53},
    # 'TypeScript': {'category': 1, 'width': 85},
    # 'Rust': {'category': 1, 'width': 55},
    # 'Scala': {'category': 1, 'width': 58},
    # 'Perl': {'category': 1, 'width': 51},
    # 'R': {'category': 1, 'width': 37},
    # 'Dart': {'category': 1, 'width': 55},
    # 'Haskell': {'category': 1, 'width': 68},
    # 'MATLAB': {'category': 1, 'width': 74},
    'SQL': {'category': 1, 'width': 52},

    # Frontend Frameworks
    'React': {'category': 2, 'width': 58},
    # 'Angular': {'category': 2, 'width': 71},
    'Vue': {'category': 2, 'width': 51},
    'Svelte': {'category': 2, 'width': 63},
    'Next': {'category': 2, 'width': 57},
    # 'Nuxt': {'category': 2, 'width': 57},
    # 'Gatsby': {'category': 2, 'width': 68},

    # Backend Frameworks
    'Node': {'category': 3, 'width': 59},
    'Express': {'category': 3, 'width': 70},
    # 'Django': {'category': 3, 'width': 70},
    'Flask': {'category': 3, 'width': 58},
    # 'Rails': {'category': 3, 'width': 56},
    # 'Spring': {'category': 3, 'width': 68},
    # '.NET': {'category': 3, 'width': 57},
    'Laravel': {'category': 3, 'width': 68},
    # 'Phoenix': {'category': 3, 'width': 70},

    # Web Technologies
    'HTML5': {'category': 4, 'width': 68},
    'CSS3': {'category': 4, 'width': 57},
    'Sass': {'category': 4, 'width': 57},
    # 'LESS': {'category': 4, 'width': 57},
    # 'Bootstrap': {'category': 4, 'width': 85},
    'Tailwind CSS': {'category': 4, 'width': 100},

    # Databases
    'MySQL': {'category': 5, 'width': 66},
    # 'PostgreSQL': {'category': 5, 'width': 91},
    'MongoDB': {'category': 5, 'width': 84},
    'SQLite': {'category': 5, 'width': 66},
    'Oracle': {'category': 5, 'width': 66},
    # 'Redis': {'category': 5, 'width': 58},
    # 'Cassandra': {'category': 5, 'width': 86},
    'Firebase': {'category': 5, 'width': 76},
    # 'Elastic': {'category': 5, 'width': 66},
    
    # DevOps Tools
    # 'Jenkins': {'category': 6, 'width': 68},
    # 'Travis CI': {'category': 6, 'width': 74},
    # 'CircleCI': {'category': 6, 'width': 75},
    'GitLab CI': {'category': 6, 'width': 80},
    'GitHub Actions': {'category': 6, 'width': 108},
    # 'Ansible': {'category': 6, 'width': 70},
    # 'Terraform': {'category': 6, 'width': 83},
    # 'Chef': {'category': 6, 'width': 57},
    # 'Puppet': {'category': 6, 'width': 70},

    # Version Control
    'Git': {'category': 7, 'width': 48},
    # 'Subversion': {'category': 7, 'width': 86},
    # 'Mercurial': {'category': 7, 'width': 80},

    # Cloud Platforms
    'AWS': {'category': 8, 'width': 54},
    # 'Google Cloud': {'category': 8, 'width': 103},
    'Azure': {'category': 8, 'width': 62},
    # 'IBM Cloud': {'category': 8, 'width': 85},
    # 'Heroku': {'category': 8, 'width': 73},
    # 'DigitalOcean': {'category': 8, 'width': 97},

    # Project Management Tools
    'Jira': {'category': 9, 'width': 49},
    'Trello': {'category': 9, 'width': 60},
    # 'Asana': {'category': 9, 'width': 62},
    'Slack': {'category': 9, 'width': 58},
    # 'Confluence': {'category': 9, 'width': 90},
    # 'Basecamp': {'category': 9, 'width': 85},

    # Virtualization Tools
    'Docker': {'category': 10, 'width': 72},
    # 'Kubernetes': {'category': 10, 'width': 92},
    # 'Vagrant': {'category': 10, 'width': 72},
    'VirtualBox': {'category': 10, 'width': 83},

    # Operating Systems
    'Linux': {'category': 11, 'width': 58},
    'Windows': {'category': 11, 'width': 78},
    # 'macOS': {'category': 11, 'width': 68},

    # APIs and Protocols
    # 'GraphQL': {'category': 12, 'width': 77},
    'APIs': {'category': 12, 'width': 55},
    # 'SOAP': {'category': 12, 'width': 58},
    'WebSockets': {'category': 12, 'width': 94},
    # 'OAuth': {'category': 12, 'width': 66},
    'JWT': {'category': 12, 'width': 53},
    # 'WebAssembly': {'category': 12, 'width': 107},
}

tag_names = shuffle_dictionary(TECHNOLOGIES) if RANDOM_TAGS else TECHNOLOGIES

__all__ = ['TAG_PADDING', 'TAG_HEIGHT', 'IMG_HEIGHT', 'LANGUAGES', 'COLORS', 'CATEGORIES', 'tag_names', 'SVG_TAG_WIDTH', 'color']
