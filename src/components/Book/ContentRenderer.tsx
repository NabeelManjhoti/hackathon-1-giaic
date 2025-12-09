import React from 'react';
import clsx from 'clsx';
import styles from './ContentRenderer.module.css';

interface ContentRendererProps {
  title: string;
  content: string;
  className?: string;
}

const ContentRenderer: React.FC<ContentRendererProps> = ({
  title,
  content,
  className = ''
}) => {
  return (
    <div className={clsx(styles.contentRenderer, className)}>
      <div className="robotic-panel">
        <div className="robotic-geometry-content">
          <header className={styles.contentHeader}>
            <h1 className={clsx('robotic-text-glow', styles.contentTitle)}>{title}</h1>
          </header>

          <div className={styles.contentBody}>
            {/* In a real implementation, this would render the actual MDX content */}
            {/* For now, we'll render the content as a placeholder */}
            <div className={styles.textContent}>
              {content}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ContentRenderer;