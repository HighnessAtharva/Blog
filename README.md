**Support me here if you liked this!**
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/AtharvaShah)

## Blog

My very own personal blog where I ruminate about technology, programming, books, entertainment and all the fine things in life. Currently hosted on Netlify but I sure do want my own domain for it some day. Hoping it blows up.

![mywebsite](https://user-images.githubusercontent.com/68660002/180614089-ed51c89d-7948-49f0-aa3f-6f9ef50fbdcc.JPG)

## Commands

```shell
# make a new post  (posts/ is a directory, either make choose your own series directory or skip altogether. A basic md file will be generated in the contents folder)
hugo new posts/my-first-post.md

# start local development server with live preview. Add static files to the static folder first otherwise you may have to restart server when files are not found
hugo server -D

# generate public content based on new additions (in the public/ folder)
hugo

# push to gihub and ensure Netlify deployment is set to auto -> blog site will be updated in a few moments.
```

## Shortcodes

### Fancy Link

```md
 {{< fancylink "Want to know my thoughts about the Watchmen Comic Series?" "Read my full review here" "/posts/personal/book-review/watchmen-comic-review/" >}}
```

### Gallery

```md
{{< galleries >}}
{{< gallery src="/blog/django-testing-1.png" title="Why Test">}}
{{< gallery src="/blog/django-testing-2.png" title="Testing Types">}}
{{< gallery src="/blog/django-testing-3.png" title="Why Test">}}
{{< gallery src="/blog/django-testing-4.png" title="Blame!" >}}
{{< /galleries >}}
```

### Highlight

```md
This is the {{< highlight "most trending" >}} post of the decade.
```

### Images with Caption

Here, 1000 Gecs is the caption that will appear below the image. Text between strings also supports markdown.

```md
![Alt should always be set for reasons of inclusion](/blog/django-testing-4.png "1000 Gecs")
```

### Blockquote

```md
Normal quote:
{{< blockquote >}}
  This is a simple quote.
{{< /blockquote >}}

Quote with author
{{< blockquote author="Author2" >}}
  This is a quote with only an Author named Author2.
{{< /blockquote >}}

Quote with author and source
{{< blockquote author="Author3" source="Source" >}}
  This is a quote from Author3 and source "source."
{{< /blockquote >}}

Quote with author and link
{{< blockquote author="Author4" link="https://www.google.com" >}}
  This is a quote from Author4 and links to https://www.google.com.
{{< /blockquote >}}

Quote with author, link and title
{{< blockquote author="Author5" link="https://www.google.com" title="Google" >}}
  This is a quote from Author5 and links to https://www.google.com with title "Google."
{{< /blockquote >}}
```

### Tweet

```md
{{< tweet user="SanDiegoZoo" id="1453110110599868418" >}}
```

### YouTube

```md
{{< youtube w7Ft2ymGmfc >}}
```

### Spotify

```md
Album 
{{< spotify type="album" id="6bQkurEvgWIUUvKeqaJRq2" >}}

Track
{{< spotify type="track" id="3dsz3hT88uR2RJhtegnilY" >}}

Artist
{{< spotify type="artist" id="00FQb4jTyendYWaN8pK0wa" >}}

Playlist 
{{< spotify type="playlist" id="37i9dQZF1DX6dvuioZhoLo" >}}



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
