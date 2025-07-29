# JokeAPI v2 MCP Server README

## Overview

The JokeAPI v2 MCP server is a powerful REST API designed to provide uniformly formatted jokes. This service is accessible without the need for API tokens, memberships, registrations, or payments. The API is highly flexible, offering a variety of filters to help you obtain the specific jokes you need. It supports multiple response formats, including JSON, XML, YAML, and plain text, making it versatile for various applications.

## Features

- **Uniformly Formatted Jokes**: Retrieve jokes that are consistently formatted for easy integration into your applications.
- **Flexible Filtering**: Utilize a wide range of filters to tailor the jokes to your specific needs, ensuring you get exactly what you're looking for.
- **Multiple Formats**: Choose from JSON, XML, YAML, or plain text formats to suit your application's requirements.
- **No Authentication Required**: Access the jokes without the hassle of setting up API tokens or user accounts.
- **Free Access**: Enjoy the service without any cost, making it accessible for both hobbyists and professionals alike.

## Endpoints

### Main Endpoints

- **Get Joke**: This is the primary endpoint to call when you want to retrieve a joke. It supports various parameters to customize the type of joke you receive, such as joke type, format, and blacklist flags.

- **Info**: Provides essential information about the JokeAPI, including its capabilities and current status.

- **Submit Joke**: Allows users to submit their own jokes for review. Approved jokes will be added to the official JokeAPI collection.

### Other Endpoints

- **Categories**: Returns a list of all available joke categories, helping you narrow down your joke search by specific themes or genres.

- **Ping**: Useful for uptime monitoring, this endpoint ensures the API is operational. You can also utilize it for basic connectivity checks.

- **Flags**: Provides a list of all available blacklist flags, allowing you to filter out jokes that might not be suitable for all audiences.

- **Formats**: Returns a list of all available response formats, so you can easily select the right format for your application.

## Tool Descriptions

- **Get Joke**: Customize your joke retrieval with parameters like `type`, `format`, `contains`, `idRange`, `blacklistFlags`, and `safe_mode` to ensure you get the perfect joke for your needs.

- **Info**: Learn more about the API's features and current operational status.

- **Submit Joke**: Contribute your own jokes to the community by submitting them through this endpoint.

- **Categories**: Explore the different joke categories available and find the one that fits your mood or audience.

- **Ping**: Verify the API's uptime and connectivity with this simple endpoint.

- **Flags**: Understand the available blacklist flags to filter jokes appropriately for different audiences.

- **Formats**: Choose the right response format for your joke retrieval to integrate seamlessly into your application.

Thank you for using JokeAPI v2! Enjoy a seamless experience with well-formatted jokes and flexible customization options.