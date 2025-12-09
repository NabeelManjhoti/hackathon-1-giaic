# Quickstart Guide: GIAIC Robotix Landing Page & Book

**Feature**: GIAIC Robotix Landing Page & Book
**Date**: 2025-12-10

## Getting Started

### Prerequisites
- Node.js 18 or higher
- npm or yarn package manager
- Git for version control

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
npm install
# or
yarn install
```

3. Start the development server:
```bash
npm run start
# or
yarn start
```

4. Open your browser to `http://localhost:3000` to view the site.

### Configuration

1. Update the Docusaurus configuration in `docusaurus.config.ts`:
   - Site title and description
   - Theme colors and navigation
   - Social links and metadata

2. Configure AI service credentials (if using AI content generation):
   - Create a `.env` file with your API keys
   - Add `OPENAI_API_KEY` for content and image generation

## Development Workflow

### Adding a New Chapter
1. Create a new MDX file in the `docs/book/` directory
2. Follow the MDX format with appropriate frontmatter
3. Add the chapter to the sidebar configuration in `sidebars.ts`

### Customizing the Theme
1. Modify CSS in the `src/theme/` directory
2. Update color variables in the Docusaurus config
3. Create custom React components in `src/components/`

### Adding Robotic Animations
1. Create new animation components in `src/components/LandingPage/`
2. Use Framer Motion for complex animations
3. Ensure animations align with the robotic aesthetic

## Building for Production

```bash
npm run build
# or
yarn build
```

The built site will be available in the `build/` directory and can be deployed to any static hosting service.

## Key Files and Directories

- `docusaurus.config.ts` - Main site configuration
- `src/pages/index.tsx` - Landing page
- `docs/book/` - Book content in MDX format
- `src/components/` - React components for animations and UI
- `src/theme/` - Custom theme and styling
- `static/img/` - Static images including generated content