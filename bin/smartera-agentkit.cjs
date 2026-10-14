#!/usr/bin/env node
'use strict';

const { spawnSync } = require('node:child_process');
const path = require('node:path');
const { constants } = require('node:os');
const { existsSync } = require('node:fs');
const { agentkitWheel } = require('../package.json');

// Resolve the bundled wheel relative to this launcher, preserving the caller's
// working directory so that an omitted target still means the caller's project.
const wheel = path.resolve(__dirname, '..', agentkitWheel);
if (!existsSync(wheel)) {
  console.error('smartera-agentkit: bundled wheel is missing. Run "uv build --wheel" in the AgentKit checkout.');
  process.exit(1);
}
const result = spawnSync(
  'uvx',
  ['--from', wheel, 'smartera-agentkit', ...process.argv.slice(2)],
  { stdio: 'inherit', shell: false },
);

if (result.error) {
  console.error(result.error.code === 'ENOENT'
    ? 'smartera-agentkit: uvx is required. Install uv: https://docs.astral.sh/uv/getting-started/installation/'
    : `smartera-agentkit: could not launch uvx: ${result.error.message}`);
  process.exitCode = 1;
} else {
  process.exitCode = result.status ?? (128 + (constants.signals[result.signal] || 1));
}
