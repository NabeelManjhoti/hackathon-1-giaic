import React, { JSX } from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import RoboticAnimation from '@site/src/components/LandingPage/RoboticAnimation';
import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title robotic-text-glow robotic-text-pulse robotic-float">GIAIC Robotix</h1>
        <p className="hero__subtitle robotic-font-light">Physical AI & Humanoid Robotics <br /> By M Nabeel Ali</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg robotic-button robotic-button-primary robotic-float"
            to="/docs/book/cover">
            Explore Book
          </Link>
          <Link
            className="button button--outline button--lg robotic-button robotic-button-secondary"
            to="/docs/book/chapter-1">
            Start Reading
          </Link>
        </div>
      </div>
    </header>
  );
}

// Robotic Feature Card Component
interface RoboticFeatureCardProps {
  title: string;
  description: string;
  icon: string;
  delay?: number;
}

function RoboticFeatureCard({ title, description, icon, delay = 0 }: RoboticFeatureCardProps) {
  return (
    <div
      className="col col--4"
      style={{ animationDelay: `${delay}s` }}
    >
      <div className="robotic-panel robotic-card padding--lg text--center robotic-scale">
        <div className="robotic-icon robotic-rotate" style={{
          backgroundImage: `url('data:image/svg+xml,<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"%2300f7ff\" stroke-width=\"2\"><path d=\"${icon}\"></path></svg>')`,
          margin: '0 auto 1rem',
          width: '48px',
          height: '48px'
        }}></div>
        <h3 className="robotic-font">{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

// Advanced Robotic Grid Section
function AdvancedRoboticGrid() {
  const features = [
    {
      title: 'Physical AI',
      description: 'Advanced artificial intelligence in robotics applications',
      icon: 'M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z'
    },
    {
      title: 'Humanoid Systems',
      description: 'Next-generation humanoid robotics and control systems',
      icon: 'M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-4m-5 0h-4m0 0h-4m0 0h-4m4 0V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-4'
    },
    {
      title: 'Future Tech',
      description: 'Cutting-edge robotics and automation technologies',
      icon: 'M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4'
    }
  ];

  return (
    <section className={clsx('futuristic-grid', styles.roboticGridSection)}>
      <div className="container padding-horiz--md">
        <div className="text--center padding-bottom--lg">
          <h2 className="robotic-font robotic-text-glow">Core Technologies</h2>
          <p className="robotic-font-light">Explore the cutting-edge technologies powering the future of robotics</p>
        </div>
        <div className="row">
          {features.map((feature, index) => (
            <RoboticFeatureCard
              key={index}
              title={feature.title}
              description={feature.description}
              icon={feature.icon}
              delay={index * 0.2}
            />
          ))}
        </div>
      </div>
    </section>
  );
}

// Robotic Stats Section
function RoboticStats() {
  const stats = [
    { value: '10+', label: 'AI Models' },
    { value: '50+', label: 'Robotic Systems' },
    { value: '1000+', label: 'Lines of Code' }
  ];

  return (
    <section className={clsx('robotic-geometry', styles.roboticStatsSection)}>
      <div className="container padding-vert--lg">
        <div className="row">
          {stats.map((stat, index) => (
            <div key={index} className="col col--4 text--center">
              <div className="robotic-panel robotic-card padding--lg robotic-pulse" style={{ animationDelay: `${index * 0.3}s` }}>
                <h3 className="robotic-font robotic-text-glow" style={{ color: 'var(--robotic-accent-primary)' }}>{stat.value}</h3>
                <p className="robotic-font-light">{stat.label}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`GIAIC Robotix`}
      description="Physical AI & Humanoid Robotics - Exploring the Future of Artificial Intelligence and Robotics">
      {/* Robotic background animation */}
      <div className={styles.roboticBackground}>
        <RoboticAnimation />
      </div>

      <main className={styles.mainContent}>
        <HomepageHeader />

        <div className="container">
          {/* Advanced Robotic Grid */}
          <AdvancedRoboticGrid />

          {/* Robotic Stats */}
          <RoboticStats />

          {/* Additional Robotic Elements */}
          <section className={clsx('robotic-geometry', styles.additionalSection)}>
            <div className="container padding-vert--lg">
              <div className="text--center padding-bottom--lg">
                <h2 className="robotic-font robotic-text-glow">Why GIAIC Robotix?</h2>
                <p className="robotic-font-light">The future of robotics is here</p>
              </div>

              <div className="row">
                <div className="col col--6">
                  <div className="robotic-panel robotic-card padding--lg robotic-float">
                    <h3 className="robotic-font">Advanced AI</h3>
                    <p>State-of-the-art artificial intelligence algorithms designed for physical systems and real-world applications.</p>
                  </div>
                </div>
                <div className="col col--6">
                  <div className="robotic-panel robotic-card padding--lg robotic-float" style={{ animationDelay: '0.2s' }}>
                    <h3 className="robotic-font">Humanoid Design</h3>
                    <p>Biomimetic robotics inspired by human anatomy and movement patterns for enhanced mobility and interaction.</p>
                  </div>
                </div>
              </div>

              <div className="row padding-top--lg">
                <div className="col col--12">
                  <div className="robotic-panel robotic-card padding--lg text--center robotic-scale">
                    <h3 className="robotic-font robotic-text-glow">Join the Robotics Revolution</h3>
                    <p className="robotic-font-light">Explore our comprehensive guide to Physical AI and Humanoid Robotics</p>
                    <div className={styles.buttons}>
                      <Link
                        className="button button--primary robotic-button robotic-button-primary"
                        to="/docs/book/cover">
                        Start Learning
                      </Link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </main>
    </Layout>
  );
}