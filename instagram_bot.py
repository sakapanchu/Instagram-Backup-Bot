import instaloader

insta = instaloader.Instaloader()

acc = 'opswatacademy'

insta.download_profile(acc, profile_pic_only=False)
