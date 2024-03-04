import requests
import argparse
import json
import subprocess
import os
from pyfiglet import Figlet
from PyInquirer import style_from_dict, Token, prompt

f = Figlet(font='slant')

def create_settings(url, user, light_ids, fail_colour, success_colour):
    data = {
        "api_user": user,
        "url": url,
        "lights" : {
            "ids": light_ids,
            "fail_colour": fail_colour,
            "success_colour": success_colour
        }
    }
    
    home_dir = os.path.expanduser("~")

    try:
        os.mkdir('{}/.is-my-build-done'.format(home_dir))
    except FileExistsError as e:
        pass

    with open('{}/.is-my-build-done/settings.json'.format(home_dir), 'w+') as settings:
        json.dump(data, settings)
    
def get_settings():
    home_dir = os.path.expanduser("~")
    with open('{}/.is-my-build-done/settings.json'.format(home_dir), 'r') as settings:
        data = json.load(settings)
    
    return data

def check_settings():
    return os.path.exists('{}/.is-my-build-done/settings.json'.format(os.path.expanduser("~")))

def rgb_to_cie(r, g, b):
    r = int(r)
    g = int(g)
    b = int(b)

    X = 0.4124*r + 0.3576*g + 0.1805*b
    Y = 0.2126*r + 0.7152*g + 0.0722*b
    Z = 0.0193*r + 0.1192*g + 0.9505*b

    x = X / 256
    y = Y / 256

    return [round(x, 4), round(y, 4)]

def list_lights(url, user):
    resp = requests.get('{}/api/{}/lights'.format(url, user))
    lights = resp.json()
    light_names = list()
    for light in lights:
        light_data = (lights[light]["name"], light)
        light_names.append(light_data)
    
    return light_names

def get_current_colour(url, user, light_id):
    light_states = {"ids": []}
    for light in light_id:
        resp = requests.get('{}/api/{}/lights/{}'.format(url, user, light))
        resp = resp.json()

        data = resp["state"]
        ids = light_states["ids"]
        ids.append(light)
        light_states[light] = data
    return light_states

def set_light_state(url, user, states):
    ids = states["ids"]
    for light_id in ids:
        request_url = '{}/api/{}/lights/{}/state'.format(url, user, light_id)
        resp = requests.put(request_url, json=states[light_id])

def set_light(url, user, lights, colour, brightness=255):
    cie_colour = rgb_to_cie(colour["r"], colour["g"], colour["b"])
    for light in lights:
        data = {
            "on": True,
            "bri": brightness,
            "xy": cie_colour,
        }
        request_url = '{}/api/{}/lights/{}/state'.format(url, user, light)
        resp = requests.put(request_url, json=data)

def build_finished(failed):
    data = get_settings()
    url = data["url"]
    user = data["api_user"]
    lights = data["lights"]["ids"]

    if failed:
        set_light(url, user, lights, data["lights"]["fail_colour"])
    else:
        set_light(url, user, lights, data["lights"]["success_colour"])

def run_setup():
    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    })

    questions = [
        {
            'type': 'input',
            'name': 'url',
            'message': 'Enter Hue Bridge URL (include http://)'
        },
        {
            'type': 'input',
            'name': 'api_user',
            'message': 'Enter your API user code'
        },
        {
            'type': 'input',
            'name': 'fail_colour',
            'message': 'Enter Fail Colour of the form <r,g,b>'
        },
        {
            'type': 'input',
            'name': 'success_colour',
            'message': 'Enter Success Colour of the form <r,g,b>'
        }
    ]

    answers = prompt(questions, style=style)
    url = answers['url']
    user = answers['api_user']
    fail_colours = answers["fail_colour"].split(',')
    success_colours = answers["success_colour"].split(',')

    fail_colour = {
        "r": int(fail_colours[0]),
        "g": int(fail_colours[1]),
        "b": int(fail_colours[2])
    }

    success_colour = {
        "r": int(success_colours[0]),
        "g": int(success_colours[1]),
        "b": int(success_colours[2])
    }

    lights = list_lights(url, user)
    light_choices = list()
    for light in lights:
        light_choices.append({'name': light[0]})

    questions = [
        {
            'type': 'checkbox',
            'message': 'Select Lights',
            'name': 'selected_lights',
            'choices': light_choices
        }
    ]

    answers = prompt(questions, style=style)
    light_ids = list()
    for light in answers["selected_lights"]:
        for item in lights:
            if light == item[0]:
                light_ids.append(item[1])
    
    
    
    create_settings(url, user, light_ids, fail_colour, success_colour)

def main():
    parser = argparse.ArgumentParser(description='Utility for use hue bulbs to set the outcome of a bash command')

    parser.add_argument('-r', '--run', nargs='+', help='Accepts command to be run')
    parser.add_argument('-s', '--setup', action='store_true', help='Runs utility setup', required=False)

    args = parser.parse_args()

    if (args.setup):
        run_setup()
    elif (args.run):
        if(not check_settings()):
            print("No settings found please use '--setup' to create some")
            exit(0)
        settings = get_settings()
        url = settings["url"]
        user = settings["api_user"]
        lights = settings["lights"]["ids"]

        state = get_current_colour(url, user, lights)
        process = subprocess.run(args.run)
        if process.returncode == 0:
            print(f.renderText('Passed'))
            build_finished(False)
        else:
            print(f.renderText('Failed'))
            build_finished(True)
        input("Press Any Key to Terminate... ")
        set_light_state(url, user, state)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
    