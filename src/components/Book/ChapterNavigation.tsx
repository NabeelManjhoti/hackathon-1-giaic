import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './ChapterNavigation.module.css';

interface ChapterNavigationProps {
  currentChapter: string;
  chapters: Array<{
    id: string;
    title: string;
    path: string;
  }>;
  className?: string;
}

const ChapterNavigation: React.FC<ChapterNavigationProps> = ({
  currentChapter,
  chapters,
  className = ''
}) => {
  const {siteConfig} = useDocusaurusContext();
  const currentIndex = chapters.findIndex(ch => ch.id === currentChapter);
  const previousChapter = currentIndex > 0 ? chapters[currentIndex - 1] : null;
  const nextChapter = currentIndex < chapters.length - 1 ? chapters[currentIndex + 1] : null;

  return (
    <nav className={clsx(styles.chapterNavigation, className)}>
      <div className="container">
        <div className="row">
          <div className="col col--5">
            {previousChapter && (
              <Link
                to={previousChapter.path}
                className={clsx('button button--outline button--secondary robotic-button robotic-button-secondary', styles.navButton, styles.prevButton)}
              >
                ← Previous: {previousChapter.title}
              </Link>
            )}
          </div>
          <div className="col col--2">
            <Link
              to="/docs/intro"
              className={clsx('button button--outline button--secondary robotic-button robotic-button-secondary', styles.navButton, styles.homeButton)}
            >
              {siteConfig.title}
            </Link>
          </div>
          <div className="col col--5">
            {nextChapter && (
              <Link
                to={nextChapter.path}
                className={clsx('button button--outline button--secondary robotic-button robotic-button-secondary', styles.navButton, styles.nextButton)}
              >
                Next: {nextChapter.title} →
              </Link>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default ChapterNavigation;