import React from 'react';
import clsx from 'clsx';
import styles from './AnimatedIcon.module.css';

interface AnimatedIconProps {
  icon: string;
  size?: 'small' | 'medium' | 'large';
  animation?: 'pulse' | 'rotate' | 'float' | 'none';
  className?: string;
  color?: string;
}

const AnimatedIcon: React.FC<AnimatedIconProps> = ({
  icon,
  size = 'medium',
  animation = 'none',
  className = '',
  color = 'var(--robotic-accent-primary)',
}) => {
  const iconClasses = clsx(
    'robotic-icon',
    styles.animatedIcon,
    {
      [styles.small]: size === 'small',
      [styles.medium]: size === 'medium',
      [styles.large]: size === 'large',
      [styles.pulse]: animation === 'pulse',
      [styles.rotate]: animation === 'rotate',
      [styles.float]: animation === 'float',
    },
    className
  );

  // In a real implementation, we would use actual SVG icons
  // For now, we'll use a simple div with a background that represents the icon
  return (
    <div
      className={iconClasses}
      style={{
        backgroundColor: color,
        maskImage: `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='${encodeURIComponent(color)}' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 5v14M5 12h14'/%3E%3C/svg%3E")`,
        WebkitMaskImage: `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='${encodeURIComponent(color)}' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 5v14M5 12h14'/%3E%3C/svg%3E")`,
      }}
    >
      <div className={styles.iconContent}>{icon}</div>
    </div>
  );
};

export default AnimatedIcon;