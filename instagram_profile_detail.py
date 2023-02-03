from instagramy import InstagramUser
username = input("Enter username: ");
user = InstagramUser(username)
print("Followng: ",user.number_of_followers);
print("followings: ",user.number_of_followings);
print("post: ",user.number_of_posts);
print("bio: ",user.biography);
print("website: ",user.website);