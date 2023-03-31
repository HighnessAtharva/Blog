**Support me here if you liked this!**
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/AtharvaShah)

# Blog

My very own personal blog where I ruminate about technology, programming, books, entertainment and all the fine things in life. Currently hosted on Netlify but I sure do want my own domain for it some day. Hoping it blows up.

![mywebsite](https://user-images.githubusercontent.com/68660002/180614089-ed51c89d-7948-49f0-aa3f-6f9ef50fbdcc.JPG)

# Commands

```shell
# make a new post  (posts/ is a directory, either make choose your own series directory or skip altogether. A basic md file will be generated in the contents folder)

hugo new posts/my-first-post.md


# start local development server with live preview. Add static files to the static folder first otherwise you may have to restart server when files are not found

hugo server -D


# generate public content based on new additions (in the public/ folder)
hugo

# push to gihub and ensure Netlify deployment is set to auto -> blog site will be updated in a few moments.
```

## File Hierarchy

```shell
|   .gitmodules
|   .hugo_build.lock
|   config.yml                                  # Site Settings and Customization. 
| 
+---archetypes
|       default.md
|       
+---assets                                       # Adding Custom CSS
|   \---css
|       \---core
|               theme-vars.css 
|               
+---content                                      # Site Content
|   |   about.md
|   |   archives.md
|   |   privacy policy.md
|   |   search.md
|   |   
|   \---blog                                     # Folder Hierarchy for Better Maintainece
|       +---Book Quotes
|       |       The Best Quotes from Book of the Ancestors Trilogy by Mark Lawrence.md
|       |       The Best Quotes from Broken Empire Trilogy by Mark Lawrence.md
|       |       ...
|       |       
|       \---DSA-Python
|               1. Arrays.md                      # Markdown Files are posts
|               2. Backtracking.md
|               3. Elementry Algos.md
|               ...
|               
+---data
+---layouts                                        # Overriding Theme Settings
|   +---partials
|   |       comments.html
|   |       disqus.html                            # Adding My Very Own Comment Section
|   |       extend_head.html
|   |       footer.html
|   |       
|   \---_default
|           archives.html
|           search.html
|           
+---mobile-notes                                   # Custom folder for syncing mobile notes to Repo
|       .gitignore
|       Ms Marvel Review.md
|       
+---public
+---resources
|   \---_gen
|       +---assets
|       \---images
+---static                                          # Storing Favicons, Site Images and Blog Post Covers
|   |   android-chrome-192x192.png
|   |   android-chrome-512x512.png
|   |   apple-touch-icon.png
|   |   favicon-16x16.png
|   |   favicon-32x32.png
|   |   favicon.ico
|   |   site.webmanifest
|   |   
|   +---about
|   |       aboutcover.jpeg
|   |       
|   +---blog
|   |   \---dsa
|   |           array.jpg
|   |           backtracking.jpg
|   |           binary-tree.jpg
|   |           bst.jpg
|   |           dp.jpg
|   |           ...
|   |           
|   \---profile
|           header_button.gif
|           profile_icon.gif
|           
\---themes                                          # Theme Folder (Not to be modified)
    \---PaperMod
```
