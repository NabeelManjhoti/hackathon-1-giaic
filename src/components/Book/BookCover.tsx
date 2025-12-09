import React, { useState, useEffect } from 'react';
import clsx from 'clsx';
import styles from './BookCover.module.css';
import { AIContentGenerator } from '@site/src/utils/ai-content-generator';

interface BookCoverProps {
  title?: string;
  author?: string;
  className?: string;
}

const BookCover: React.FC<BookCoverProps> = ({
  title = 'GIAIC Robotix: Physical AI & Robotics',
  author = 'Nabeel Manjhoti',
  className = ''
}) => {
  const [coverUrl, setCoverUrl] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<boolean>(false);

  useEffect(() => {
    const generateCover = async () => {
      try {
        setLoading(true);
        // In a real implementation, this would call an actual AI image generation service
        // For now, we'll use a placeholder that represents the generated image
        const generatedUrl = await AIContentGenerator.generateBookCover({
          title,
          theme: 'futuristic-robotic',
          colors: ['00f7ff', '00b3ff', '1a1a22'],
          style: 'tech-cyberpunk'
        });

        setCoverUrl(generatedUrl);
      } catch (err) {
        console.error('Error generating book cover:', err);
        setError(true);
        // Fallback cover
        setCoverUrl(`https://placehold.co/400x600/1a1a22/00f7ff?text=${encodeURIComponent(title)}&font=orbitron`);
      } finally {
        setLoading(false);
      }
    };

    generateCover();
  }, [title]);

  return (
    <div className={clsx(styles.bookCoverContainer, className)}>
      <div className={clsx('robotic-panel', styles.bookCoverWrapper)}>
        {loading ? (
          <div className={clsx('robotic-loader', styles.loader)}>
            <div></div>
            <div></div>
          </div>
        ) : error ? (
          <div className={styles.errorPlaceholder}>
            <div className={styles.errorIcon}>⚠️</div>
            <p>Failed to generate cover image</p>
          </div>
        ) : (
          <div className={styles.bookCover}>
            <img
              src={coverUrl}
              alt={`${title} cover`}
              className={styles.coverImage}
              onError={() => setError(true)}
            />
          </div>
        )}

        <div className={styles.bookInfo}>
          <h2 className={clsx('robotic-text-glow', styles.bookTitle)}>{title}</h2>
          <p className={styles.bookAuthor}>by {author}</p>
        </div>
      </div>
    </div>
  );
};

export default BookCover;