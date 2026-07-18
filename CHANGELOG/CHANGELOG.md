# Change Log

## Version-0.1 | Foundation |  10 July 2026

### User Features
- Homepage displaying notable quotes
- Quote database

### Engineering
- Django project setup
- Quote model
- JSON import command
- Duplicate detection during import
- Django Admin integration

<img src="v-0.1/quotes-1.png" alt="quotes list" style="display: inline-block; height: auto; width: auto; vertical-align: text-bottom; margin: 0 5px;" />

<img src="v-0.1/quotes-2.png" alt="quotes list" style="display: inline-block; height: auto; width: auto; vertical-align: text-bottom; margin: 0 5px;" />


## Version-0.2 | User Experience | 17 July 2026

Added:
- Bootstrap card-based quote layout
- Responsive quote grid
- Individual quote cards with improved typography
- Reusable template structure for quote presentation
- Improved homepage user interface

Changed:
- Replaced blockquote list with card-based layout
- Improved readability and visual presentation

<img src="v-0.2/quotes-cards.png" alt="quotes list" style="display: inline-block; height: auto; width: auto; vertical-align: text-bottom; margin: 0 5px;" />

## Version-0.3 | Author Profiles | 19 July 2026

### Author Profile Views

Added dedicated author profile pages displaying biographical information and a list of all quotes associated with each author.

This feature demonstrates Django model relationships, reverse lookups using `related_name`, and detail views for related objects.

### Database Design Notes

Version-0.3 introduced an Author model and changed Quote.author from text to a ForeignKey relationship.

This required separating author data from quote data and importing related objects before importing quotes.

<img src="v-0.3/author_profile_example.png" alt="quotes list" style="display: inline-block; height: auto; width: auto; vertical-align: text-bottom; margin: 0 5px;" />
