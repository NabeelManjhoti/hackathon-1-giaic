import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import styles from './FuturisticButton.module.css';

interface FuturisticButtonProps {
  href?: string;
  to?: string;
  children: React.ReactNode;
  variant?: 'primary' | 'secondary';
  size?: 'small' | 'medium' | 'large';
  className?: string;
  onClick?: () => void;
}

const FuturisticButton: React.FC<FuturisticButtonProps> = ({
  href,
  to,
  children,
  variant = 'primary',
  size = 'medium',
  className = '',
  onClick,
}) => {
  const buttonClasses = clsx(
    'robotic-button',
    {
      'robotic-button-primary': variant === 'primary',
      'robotic-button-secondary': variant === 'secondary',
      [styles.small]: size === 'small',
      [styles.medium]: size === 'medium',
      [styles.large]: size === 'large',
    },
    className
  );

  const buttonContent = (
    <span className={styles.buttonContent}>
      {children}
      <span className={styles.buttonGlow}></span>
    </span>
  );

  if (href) {
    return (
      <a
        href={href}
        className={buttonClasses}
        onClick={onClick}
      >
        {buttonContent}
      </a>
    );
  }

  if (to) {
    return (
      <Link
        to={to}
        className={buttonClasses}
        onClick={onClick}
      >
        {buttonContent}
      </Link>
    );
  }

  return (
    <button
      className={buttonClasses}
      onClick={onClick}
    >
      {buttonContent}
    </button>
  );
};

export default FuturisticButton;