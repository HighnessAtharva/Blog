---
title: "Food Online - Multivendor Restaurant Management"
date: 2023-07-03T19:19:34+05:30
draft: false
cover: 
    image: projects/FoodOnline.webp
    alt: 
    caption: 
description: ""
hidemeta: true
---

{{< ico "brand-github" >}} **GITHUB :** https://github.com/HighnessAtharva/FoodOnline

## Project Summary

This project, developed during a Udemy course, aims to create a multi-vendor restaurant marketplace in Ireland. The platform allows restaurant owners to register, manage their restaurant menus, receive orders, track earnings, and handle revenue payments. Customers can register, search for nearby restaurants, place orders, and purchase food from their favorite establishments. The focus of this project was on the backend development, utilizing the Django framework and various technologies to create a functional and user-friendly application.

{{< galleries >}}
{{< gallery src="/projects/FoodOnline.webp" title="Restaurant Lookup" >}}
{{< gallery src="/projects/FoodOnline2.webp" title="Restaurant Marketplace" >}}
{{< gallery src="/projects/FoodOnline3.webp" title="Vendor Registration" >}}
{{< gallery src="/projects/FoodOnline4.webp" title="Menu Page" >}}
{{< gallery src="/projects/FoodOnline5.webp" title="Checkout/Cart Page" >}}
{{< gallery src="/projects/FoodOnline6.webp" title="Paypal Integration" >}}
{{< /galleries >}}

## Project Tech Stack

- Django framework
- PostgreSQL database
- Geojdango and Google API for location-based functionalities
- FoodBakery template from Themeforest (customized for backend focus)
- Ubuntu Linode for deployment
- Nginx and Gunicorn for server configuration
- Django signals for custom user model and media files handling
- Token verification and email configuration for user registration
- CRUD functionalities for restaurant registration and authentication
- Menu builder with category and food item management
- Marketplace implementation for listing restaurants
- Google autocomplete field for address input
- PostgresSQL database configuration
- Django messages for displaying notifications
- Vendor approval process managed by the admin
- Django forms for form handling and validation
- Cart functionalities with AJAX requests for smooth user experience
- Basic and smart search functionalities for finding restaurants and food items
- Location-based search for displaying nearby restaurants on the homepage
- Dynamic tax module for accurate calculations
- Order management, checkout process, and after-order functionalities
- Integration of PayPal payment gateway
- Many-to-many relationships for linking entities
- Integrated email templates for transactional emails
- User profile settings for customization
- Deployment on Ubuntu Linode hosting server
- Gunicorn and Nginx configuration for optimized performance
- Custom domain name setup with Certbot SSL certificate configuration

## Learnings

During the development of this project, several key learnings were obtained:

- Understanding and implementation of a multi-vendor restaurant marketplace
- Utilizing Django framework for backend web development
- Integration of various technologies to enhance the user experience
- Database configuration and management with PostgreSQL
- Working with third-party APIs, such as Google Maps and PayPal
- Implementing user authentication and registration functionalities
- Customizing and extending Django templates and forms
- Handling media files and creating custom user models
- Implementing search functionalities and location-based queries
- Optimizing performance through server configuration and deployment
- Managing and securing online transactions with PayPal integration
- Working with email templates and sending transactional emails
- Handling CRUD operations and managing relationships between entities

Through this project, I gained valuable hands-on experience in building a complex web application using Django and integrating various features to create a functional and scalable multi-vendor restaurant marketplace.
