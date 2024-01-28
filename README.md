# IrvineHacks-Project
![Alt text](https://cdn.discordapp.com/attachments/1200286789416525844/1201055434115657748/zotevents_image.png?ex=65c86d0a&is=65b5f80a&hm=58fd65280ca92986c7c5c9d47cb15cbc8c142956444128c66b02b3825aa0f28f&)

Tired of not knowing where to go to meet people on UCI? Zot Events got you covered.

Our program scrapes the UCI campus groups website and parses all the inperson events for you.
Relevant information will be presented alongside an interactive map that will show you how you can get there! 

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [License](#license)
- [Credits](#credits)

## Overview

ZotEvents is a web-based platform crafted to streamline the discovery of upcoming events at the University of California, Irvine (UCI). Combining a Python backend with a JavaScript frontend built on React, ZotEvents delivers a dynamic and user-friendly experience.

Using Selenium's web scraping capabilities, ZotEvents fetches real-time information from UCI's dedicated event website, ensuring that the platform stays updated with the latest events on campus. The program efficiently manages the scraped data, organizing it in a user-friendly format that includes event names, dates, and locations. One of ZotEvents' central components is its integration with the Google Maps API. For events with location information, users can seamlessly navigate to the venue using the platform's integrated map functionality.

The workflow of ZotEvents is designed to simplify event discovery, offering the UCI community an accessible and informative tool to stay engaged with the diverse range of activities happening on campus.

## Installation

### 1. Install the Requirements.txt File

```bash
pip install -r requirements.txt
```

### 2. Confirm Chromedriver is Compatible with Your Device

Currently, Chromedriver is only installed in Windows and MacOS on the program. Make sure the executable path is correct in the scrape.py file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Credits

ZotEvents was developed by a group of beginner programmers during IrvineHacks 2024:
- [Emmanuel Bautista](https://github.com/ebautista4562) - Integrated Google Maps API for an immersive user experience, and contributed to frontend development.
- [Ethan Wong](https://github.com/txchnothunder) - Implemented dynamic web scraping using Selenium for real-time data updates, and handled backend development.
- [Leo Chao](https://github.com/twleochao) - Managed CSV, JSON files, and geocoding for efficient handling of event coordinates, and contributed to backend processes.
- [Ryan Pham](https://github.com/ryanpham17) - Designed the UI/UX for an appealing frontend, shaping the visual aesthetics of ZotEvents.
