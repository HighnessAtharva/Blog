---
title: "Awesome Hugo Shortcodes For Your Websites"
date: 2023-07-02T00:19:35+05:30
draft: false
cover: 
    image: blog/hugo-shortcodes.webp
    alt: Hugo Shortcodes
    caption: Unleashing the Potential of Hugo Shortcodes. A Step-by-Step Guide to Customization + 5 Inspiring Examples
description: "Awesome hugo shortcodes I am running to power this site. Lightweight, fast and easy to use. Everything from galleries, blockquotes, spotify embeds and more."
tags: ["technology"]
---

As a web developer, you're constantly seeking efficient ways to streamline your workflow and enhance the functionality of your websites. In this blog post, we'll explore the concept of Hugo Shortcodes, their significance, and how you can leverage them to create dynamic and reusable content in your Hugo-powered websites. Whether you're new to Hugo or looking to level up your skills, this guide will provide you with a comprehensive understanding of Hugo Shortcodes and how to effectively use them.

## What are Shortcodes?

Hugo Shortcodes are simple, reusable snippets of code that enable you to add dynamic content or functionality to your Hugo static websites. They are essentially shortcuts that allow you to avoid repetitive coding and provide a convenient way to inject complex HTML, CSS, or JavaScript into your content.

## Why do I need them?

They offer several advantages that make them a valuable tool in your web development arsenal:

- **Reusability**: Shortcodes enable you to create modular and reusable components that can be easily inserted into multiple pages or sections of your website.
- **Code Organization**: By encapsulating specific functionalities within shortcodes, you can keep your content clean and separate concerns, making it easier to maintain and update your website.
- **Enhanced Functionality**: Shortcodes allow you to extend the capabilities of your Hugo websites by adding dynamic elements such as customizable forms, interactive maps, social media embeds, and more.
- **Developer Productivity**: With the ability to encapsulate complex code snippets into simple shortcodes, you can save time and effort by avoiding repetitive coding tasks.

{{< fancylink "Tired of managing hundreds of tabs? Discover how to" "Stay Organized in Chrome" "/posts/tech/how-i-stay-organized-in-chrome/" >}}

## How to Write Custom Hugo Shortcodes?

Creating custom Hugo Shortcodes is a straightforward process. Here's a step-by-step guide to get you started:

1. Determine the functionality or content you want to encapsulate within the shortcode.
1. Navigate to the `/layouts/shortcodes` directory in your Hugo project.
1. Create a new file with a descriptive name, ending in .html (e.g. `myshortcode.html`).
1. Write the desired HTML, CSS, or JavaScript code within the file, following Hugo's templating syntax.
1. Save the file and close it.

## How to Invoke/Use Shortcodes?

Once you've created a custom Hugo Shortcode, you can easily invoke it within your Markdown content using double curly braces with the shortcode name:

```md
{{</* myshortcode */>}}
```

You can also pass parameters to your shortcodes by including key-value pairs within the opening tag:

```md
{{</* myshortcode param1="value1" param2="value2" */>}}
```

Remember to replace myshortcode with the actual name of your custom shortcode.

## Custom Shortcodes

By adding my favorite custom shortcodes and continuously expanding the collection, you can effortlessly enhance the fanciness of your website. Investing just 10 minutes in this simple and extendible process will yield remarkable results in improving the overall appeal and functionality of your site.

![Shortcode Path](/blog/shortcode-path.webp)

### Gallery

Paste the code for galleries shortcode in `layouts/shortcodes/galleries.html` and you are good to go! We use the nanogallery library to do all the good stuff for you. It will be a wraper div around the gallery shortcode.

**CODE**

{{< gist HighnessAtharva fb8f94fd557689a634203f4d34a58220 galleries.html >}}

{{< gist HighnessAtharva fb8f94fd557689a634203f4d34a58220 gallery.html >}}

**USAGE**

```md
{{</* galleries */>}}
{{</* gallery src="/blog/er-1.webp" title="Elden Ring" */>}}
{{</* gallery src="/blog/er-2.webp" title="Best Soulsborne Game" */>}}
{{</* gallery src="/blog/er-3.webp" title="Deep Lore" */>}}
{{</* gallery src="/blog/er-4.webp" title="Awesome Bosses" */>}}
{{</* gallery src="/blog/er-5.webp" title="Dark Atmosphere" */>}}
{{</* gallery src="/blog/er-6.webp" title="Perfectly Balanced Difficulty" */>}}
{{</* /galleries */>}}
```

**OUTPUT**

{{< galleries >}}
{{< gallery src="/blog/er-1.webp" title="Elden Ring" >}}
{{< gallery src="/blog/er-2.webp" title="Best Soulsborne Game"  >}}
{{< gallery src="/blog/er-3.webp" title="Deep Lore" >}}
{{< gallery src="/blog/er-4.webp" title="Awesome Bosses" >}}
{{< gallery src="/blog/er-5.webp" title="Dark Atmosphere"  >}}
{{< gallery src="/blog/er-6.webp" title="Perfectly Balanced Difficulty" >}}
{{< /galleries >}}

---

### Highlight

**CODE**

{{< gist HighnessAtharva fb8f94fd557689a634203f4d34a58220 highlight.html >}}

**USAGE**

```md
I wanna highlight {{</* highlight "this particular text" */>}}. Okay, did it!
```

**OUTPUT**

I wanna highlight {{< highlight "this particular text" >}}. Okay, did it!

---

### Spotify

**CODE**

{{< gist HighnessAtharva fb8f94fd557689a634203f4d34a58220 spotify.html >}}

**USAGE**

```md
Album 
{{</* spotify type="album" id="6bQkurEvgWIUUvKeqaJRq2" */>}}

Track
{{</* spotify type="track" id="3dsz3hT88uR2RJhtegnilY" */>}}

Artist
{{</* spotify type="artist" id="00FQb4jTyendYWaN8pK0wa" */>}}

Playlist 
{{</* spotify type="playlist" id="37i9dQZF1DX6dvuioZhoLo" */>}}
```

**OUTPUT**

Album
{{< spotify type="album" id="6bQkurEvgWIUUvKeqaJRq2" >}}

Track
{{< spotify type="track" id="3dsz3hT88uR2RJhtegnilY" >}}

Artist
{{< spotify type="artist" id="00FQb4jTyendYWaN8pK0wa" >}}

Playlist
{{< spotify type="playlist" id="37i9dQZF1DX6dvuioZhoLo" >}}

---

### Blockquote

**CODE**
{{< gist HighnessAtharva fb8f94fd557689a634203f4d34a58220 blockquote.html >}}

**USAGE**

```md
Normal quote:
{{</* blockquote */>}}
  This is a simple quote.
{{</* /blockquote */>}}

Quote with author:
{{</* blockquote author="Author2" */>}}
  This is a quote with only an Author named Author2.
{{</* /blockquote */>}}

Quote with author and source:
{{</* blockquote author="Author3" source="Source" */>}}
  This is a quote from Author3 and source "source."
{{</* /blockquote */>}}

Quote with author and link:
{{</* blockquote author="Author4" link="https://www.google.com" */>}}
  This is a quote from Author4 and links to https://www.google.com.
{{</* /blockquote */>}}

Quote with author, link and title:
{{</* blockquote author="Author5" link="https://www.google.com" title="Google" */>}}
  This is a quote from Author5 and links to https://www.google.com with title "Google."
{{</* /blockquote */>}}
```

**OUTPUT**

Normal quote:
{{< blockquote >}}
  This is a simple quote.
{{< /blockquote >}}

Quote with author:
{{< blockquote author="Author2" >}}
  This is a quote with only an Author named Author2.
{{< /blockquote >}}

Quote with author and source:
{{< blockquote author="Author3" source="Source" >}}
  This is a quote from Author3 and source "source."
{{< /blockquote >}}

Quote with author and link:
{{< blockquote author="Author4" link="<https://www.google.com>" >}}
  This is a quote from Author4 and links to <https://www.google.com>.
{{< /blockquote >}}

Quote with author, link and title:
{{< blockquote author="Author5" link="<https://www.google.com>" title="Google" >}}
  This is a quote from Author5 and links to <https://www.google.com> with title "Google."
{{< /blockquote >}}

---

## Built-In Shortcodes

These useful shortcodes listed below do not require custom code or the need to create HTML files or place them in the layouts directory. Hugo provides built-in support for these shortcodes. You can explore more shortcodes by referring to the [official documentation here](https://gohugo.io/content-management/shortcodes/#use-hugos-built-in-shortcodes).

### Tweet

```md
{{</* tweet user="cutlist_dev" id="1674315545175535616" */>}}
```

{{< tweet user="cutlist_dev" id="1674315545175535616" >}}

---

### YouTube

```md
{{</* youtube dQw4w9WgXcQ */>}}
```

{{< youtube dQw4w9WgXcQ >}}

---

### Images with Caption

This is not really a shortcode, but more of a lesser know hack. Yes, you can add a caption natively to images in markdown by passing a caption right next to the image path.

```md
![Alt should always be set for reasons of inclusion](/blog/er-1.webp "Together we shall devour the very gods.")
```

![Alt should always be set for reasons of inclusion](/blog/er-2.webp "Together we shall devour the very gods.")

---

## Conclusion

Hugo Shortcodes are powerful tools that enable web developers to create dynamic, reusable content in their Hugo websites. By harnessing the reusability and enhanced functionality provided by shortcodes, you can streamline your development process and build more efficient and engaging websites. Whether you're a beginner or an experienced developer, incorporating Hugo Shortcodes into your workflow will undoubtedly elevate the quality and flexibility of your Hugo-powered projects. So go ahead, give it a try, and unlock the full potential of Hugo Shortcodes!

{{< fancylink "Learn to deploy confidently with this guide on" "Netlify CI/CD" "/posts/tech/netlify-ci-cd/" >}}
