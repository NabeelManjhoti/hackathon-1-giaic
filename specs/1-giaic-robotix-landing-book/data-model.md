# Data Model: GIAIC Robotix Landing Page & Book

**Feature**: GIAIC Robotix Landing Page & Book
**Date**: 2025-12-10

## Entities

### LandingPage
- **id**: string - Unique identifier for the landing page
- **title**: string - Main title of the landing page
- **heroContent**: object - Content for the hero section
  - heading: string - Main heading text
  - subheading: string - Subheading text
  - ctaText: string - Call-to-action button text
  - ctaLink: string - Link for the call-to-action
- **theme**: object - Theme configuration
  - darkMode: boolean - Whether dark mode is enabled
  - primaryColor: string - Primary theme color
  - accentColor: string - Accent theme color
  - fontFamily: string - Primary font family
- **animations**: array - Configuration for robotic animations
  - type: string - Type of animation (e.g., "mechanical", "precision", "ai")
  - elementId: string - ID of element to animate
  - config: object - Animation-specific configuration

### BookContent
- **id**: string - Unique identifier for the book
- **title**: string - Title of the book
- **chapters**: array - Array of book chapters
  - id: string - Unique identifier for the chapter
  - title: string - Chapter title
  - content: string - MDX content of the chapter
  - order: number - Order of the chapter in the book
  - topic: string - Topic category (e.g., "Physical AI", "Humanoid", "Kinematics")
- **coverImage**: object - Information about the cover image
  - url: string - URL to the cover image
  - altText: string - Alternative text for accessibility
  - generatedBy: string - Service used to generate the image
- **authorBio**: object - Author biography information
  - name: string - Author's name
  - title: string - Author's title/credentials
  - expertise: array - Author's areas of expertise
  - bio: string - Detailed biography text

### ThemeConfiguration
- **id**: string - Unique identifier for the theme
- **name**: string - Name of the theme (e.g., "futuristic-dark", "robotic-precision")
- **colors**: object - Color palette for the theme
  - primary: string - Primary color
  - secondary: string - Secondary color
  - background: string - Background color
  - surface: string - Surface color
  - error: string - Error color
  - success: string - Success color
  - warning: string - Warning color
- **typography**: object - Typography settings
  - fontFamily: string - Primary font family
  - fontSize: object - Font size scale
  - fontWeight: object - Font weight scale
- **animation**: object - Animation settings
  - duration: object - Animation duration scale
  - easing: object - Easing functions
  - sequence: array - Default animation sequences

### AIContentGeneration
- **id**: string - Unique identifier for the AI generation request
- **type**: string - Type of content to generate ("image", "outline", "text")
- **prompt**: string - Prompt provided to the AI service
- **parameters**: object - Parameters for the AI service
  - style: string - Style of the output
  - quality: string - Quality level
  - dimensions: object - Dimensions for images (width, height)
- **result**: object - Result from the AI service
  - content: string - Generated content
  - url: string - URL if content is an image
  - metadata: object - Additional metadata about the generation
- **createdAt**: Date - When the request was made
- **status**: string - Status of the generation ("pending", "completed", "failed")