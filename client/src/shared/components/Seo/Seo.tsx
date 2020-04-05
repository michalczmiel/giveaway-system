import Head from "next/head";
import React from "react";

interface SeoConfig {
  title: string;
  description: string;
  favicon: string;
  url: string;
}

interface SeoProps {
  config: SeoConfig;
}

function Seo({ config }: SeoProps) {
  return (
    <Head>
      <title>{config.title}</title>
      <meta name="description" content={config.description} />
      <link rel="icon" type="image/png" sizes="32x32" href={config.favicon} />
      <meta property="og:url" content={config.url} />
      <meta property="og:title" content={config.title} />
      <meta property="og:description" content={config.description} />
      <meta property="og:type" content="website" />
    </Head>
  );
}

export default Seo;
