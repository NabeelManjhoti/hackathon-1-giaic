import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './HeroSection.module.css';

const HeroSection = () => {
  const {siteConfig} = useDocusaurusContext();

  return (
    <section className={clsx('hero', 'hero--primary', styles.heroBanner)}>
      <div className="container">
        <div className="row">
          <div className="col col--6">
            <h1 className={clsx('hero__title', 'robotic-text-glow', 'robotic-text-pulse')}>
              {siteConfig.title}
            </h1>
            <p className="hero__subtitle">{siteConfig.tagline}</p>
            <div className={styles.buttons}>
              <Link
                className={clsx(
                  'button button--secondary button--lg robotic-button robotic-button-primary',
                  styles.button,
                )}
                to="/docs/intro">
                Explore Robotics
              </Link>
              <Link
                className={clsx(
                  'button button--outline button--lg robotic-button robotic-button-secondary',
                  styles.button,
                )}
                to="/docs/book/chapter-1">
                Read Book
              </Link>
            </div>
          </div>
          <div className="col col--6">
            <div className={clsx('robotic-panel', 'robotic-geometry', styles.heroImage)}>
              <div className={styles.roboticGraphic}>
                <div className={clsx('robotic-float', styles.roboticArm)}>
                  <div className={styles.joint}></div>
                  <div className={styles.arm}></div>
                  <div className={styles.hand}></div>
                </div>
                <div className={clsx('robotic-rotate', styles.circuitBoard)}>
                  <div className={styles.circuitPattern}></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;