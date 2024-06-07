import instaloader

# Create an instance of Instaloader
insta = instaloader.Instaloader()

# Specify the Instagram account username
acc = 'opswatacademy'

# Download the profile data
insta.download_profile(acc, profile_pic_only=False)
