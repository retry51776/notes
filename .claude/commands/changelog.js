#!/usr/bin/env node

const fs = require('fs');
const { execSync } = require('child_process');
const path = require('path');

/**
 * Custom Claude command: /changelog
 * Appends changes to CHANGELOG.md with current date as section header and creates git commit
 */

function getCurrentDate() {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0');
  const day = String(now.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

function updateChangelog(changes) {
  const changelogPath = path.join(process.cwd(), 'CHANGELOG.md');
  const currentDate = getCurrentDate();
  
  try {
    let content = '';
    
    // Read existing changelog or create basic structure
    if (fs.existsSync(changelogPath)) {
      content = fs.readFileSync(changelogPath, 'utf8');
    } else {
      content = '# Changelog\n\nAll notable changes to this project will be documented in this file.\n\n';
    }
    
    // Check if there's already a section for today
    const todaySection = `## ${currentDate}`;
    const lines = content.split('\n');
    let insertIndex = -1;
    let existingTodayIndex = -1;
    
    // Find where to insert new section or if today's section already exists
    for (let i = 0; i < lines.length; i++) {
      if (lines[i].startsWith('## ')) {
        if (lines[i] === todaySection) {
          existingTodayIndex = i;
          break;
        }
        if (insertIndex === -1) {
          insertIndex = i;
        }
      }
    }
    
    // If no existing sections found, insert after header
    if (insertIndex === -1) {
      for (let i = 0; i < lines.length; i++) {
        if (lines[i].startsWith('# ')) {
          insertIndex = i + 2; // Insert after header and empty line
          break;
        }
      }
    }
    
    if (existingTodayIndex !== -1) {
      // Add to existing today section
      let insertPoint = existingTodayIndex + 1;
      // Find the end of this section (next ## or end of file)
      while (insertPoint < lines.length && !lines[insertPoint].startsWith('## ')) {
        insertPoint++;
      }
      
      // Insert before the next section or at the end
      const changeLines = changes.split('\n').filter(line => line.trim());
      const formattedChanges = changeLines.map(change => 
        change.startsWith('- ') ? change : `- ${change}`
      );
      
      lines.splice(insertPoint, 0, ...formattedChanges, '');
    } else {
      // Create new section for today
      const changeLines = changes.split('\n').filter(line => line.trim());
      const formattedChanges = changeLines.map(change => 
        change.startsWith('- ') ? change : `- ${change}`
      );
      
      const newSection = [
        todaySection,
        '',
        ...formattedChanges,
        ''
      ];
      
      lines.splice(insertIndex, 0, ...newSection);
    }
    
    // Write updated content
    fs.writeFileSync(changelogPath, lines.join('\n'));
    console.log(`✓ Updated CHANGELOG.md with changes for ${currentDate}`);
    
    return changelogPath;
  } catch (error) {
    console.error('Error updating changelog:', error.message);
    process.exit(1);
  }
}

function createGitCommit() {
  try {
    // Add changelog to git
    execSync('git add CHANGELOG.md', { stdio: 'inherit' });
    
    // Create commit with standard message
    const commitMessage = `docs: update changelog for ${getCurrentDate()}

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>`;
    
    execSync(`git commit -m "${commitMessage}"`, { stdio: 'inherit' });
    console.log('✓ Created git commit for changelog update');
  } catch (error) {
    console.error('Error creating git commit:', error.message);
    process.exit(1);
  }
}

function main() {
  const args = process.argv.slice(2);
  
  if (args.length === 0) {
    console.log('Usage: /changelog <change description>');
    console.log('Example: /changelog "Added new feature for user authentication"');
    process.exit(1);
  }
  
  const changes = args.join(' ');
  
  // Update changelog
  updateChangelog(changes);
  
  // Create git commit
  createGitCommit();
  
  console.log('✓ Changelog updated and committed successfully!');
}

main();