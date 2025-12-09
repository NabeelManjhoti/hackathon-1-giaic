import React, { JSX } from 'react';
import clsx from 'clsx';
import styles from './RoboticCard.module.css';

interface RoboticCardProps {
  children: React.ReactNode;
  className?: string;
  glow?: boolean;
  pulse?: boolean;
}

export default function RoboticCard({
  children,
  className,
  glow = false,
  pulse = false,
}: RoboticCardProps): JSX.Element {
  const roboticCardClasses = clsx(
    'robotic-card',
    'robotic-panel',
    styles.roboticCard,
    {
      'robotic-glow': glow,
      'robotic-pulse': pulse,
    },
    className
  );

  return (
    <div className={roboticCardClasses}>
      {children}
    </div>
  );
}