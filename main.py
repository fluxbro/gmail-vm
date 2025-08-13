from requests import Session
import random
import re
# https://osintcat.ru https://osintcat.ru https://osintcat.ru https://osintcat.ru https://osintcat.ru https://osintcat.ru https://osintcat.ru
def gmail(email):
    try:
        mail = re.search(r'(.+?)@', email).group(1)
        N = ''.join((random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(5, 10))))
        B = (random.randrange(1980, 2010), random.randrange(1, 12), random.randrange(1, 28))
        sess = Session()

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://accounts.google.com/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-browser-channel': 'stable',
            'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
            'x-browser-year': '2024'
        }

        params = {
            'biz': 'false',
            'continue': 'https://mail.google.com/mail/u/0/',
            'ddm': '1',
            'emr': '1',
            'flowEntry': 'SignUp',
            'flowName': 'GlifWebSignIn',
            'followup': 'https://mail.google.com/mail/u/0/',
            'osid': '1',
            'service': 'mail'
        }

    
        response = sess.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)

        if response.status_code != 200:
            return None

        if 'TL=' not in response.url:
            return None

        tl = response.url.split('TL=')[1]

        if '\"Qzxixc\":\"' not in response.text or '\"SNlM0e\":\"' not in response.text:
            return None

        s1 = response.text.split('\"Qzxixc\":\"')[1].split('\"')[0]
        at = response.text.split('\"SNlM0e\":\"')[1].split('\"')[0]

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-goog-ext-278367001-jspb': '[\"GlifWebSignIn\"]',
            'x-goog-ext-391502476-jspb': f'[\"{s1}\"]',
            'x-same-domain': '1'
        }

        params = {
            'rpcids': 'E815hb',
            'source-path': '/lifecycle/steps/signup/name',
            'hl': 'en-US',
            'TL': tl,
            'rt': 'c'
        }

        data = f'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{N}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'

        response = sess.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data
        ).text

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-goog-ext-278367001-jspb': '[\"GlifWebSignIn\"]',
            'x-goog-ext-391502476-jspb': f'[\"{s1}\"]',
            'x-same-domain': '1'
        }

        params = {
            'rpcids': 'eOY7Bb',
            'source-path': '/lifecycle/steps/signup/birthdaygender',
            'hl': 'en-US',
            'TL': tl,
            'rt': 'c'
        }

        data = f'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{B[0]}%2C{B[1]}%2C{B[2]}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3C...%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'

        response = sess.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data
        ).text

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-goog-ext-278367001-jspb': '[\"GlifWebSignIn\"]',
            'x-goog-ext-391502476-jspb': f'[\"{s1}\"]',
            'x-same-domain': '1'
        }

        params = {
            'rpcids': 'NHJMOd',
            'source-path': '/lifecycle/steps/signup/username',
            'hl': 'en-US',
            'TL': tl,
            'rt': 'c'
        }

        data = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{mail}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'

        R = sess.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data
        ).text
        if 'password' in R:
            return True #Available
        return False #Taken
    except:
        return None #Error

a = gmail("flux@gmail.com")
