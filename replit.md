# CryptoBuddy - A Friendly Crypto Chatbot

## Overview

CryptoBuddy is a Python-based cryptocurrency recommendation chatbot designed to provide friendly, accessible guidance to users exploring cryptocurrency investments. The application features a conversational interface with a playful personality that helps users discover cryptocurrencies based on their preferences for profitability and sustainability. The bot uses a predefined cryptocurrency database to make recommendations and provide investment advice tailored to user goals.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Core Application Structure
The application follows a simple object-oriented design with a single main class `CryptoBuddy` that encapsulates all chatbot functionality. This monolithic approach keeps the codebase simple and easy to understand for a lightweight recommendation system.

### Data Storage Design
The application uses an in-memory dictionary (`crypto_db`) to store cryptocurrency information, eliminating the need for external databases or file I/O operations. Each cryptocurrency entry contains structured data including price trends, market capitalization, energy usage, and sustainability scores, providing a foundation for recommendation algorithms.

### Recommendation Engine
The bot implements rule-based recommendation logic using conditional statements to filter cryptocurrencies based on user criteria:
- **Profitability recommendations**: Prioritize cryptocurrencies with "rising" price trends and "high" market capitalization
- **Sustainability recommendations**: Focus on cryptocurrencies with "low" energy usage and sustainability scores above 7/10

### User Interface Pattern
The application uses a command-line interface with conversational flow, featuring randomized greetings to create a more engaging user experience. The bot processes natural language queries and maps them to predefined recommendation categories.

### Personality System
The chatbot incorporates personality through randomized greeting messages and a friendly, approachable tone throughout interactions. This design choice makes cryptocurrency information more accessible to newcomers while maintaining an educational focus.

## External Dependencies

The application currently has minimal external dependencies:
- **Python Standard Library**: Uses the `random` module for greeting message randomization
- **No External APIs**: The system operates entirely offline using predefined data
- **No Database Systems**: All data is stored in-memory using Python dictionaries
- **No Web Frameworks**: Designed as a console application without web interface requirements