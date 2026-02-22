# Double Jump Feature - Implementation Guide

## Overview
A cool double jump mechanic has been added to the **JUMPING ENGINEER** game with a 10-second cooldown timer between uses.

## How It Works

### Activation
- **Press SPACE, UP ARROW, or W** while in the air to perform a double jump
- The double jump can only be used once per jump session (after you leave the ground)
- Once used, a **10-second cooldown** begins before you can use it again

### Cooldown System
- After performing a double jump, the ability enters a 10-second cooldown period
- You can still perform regular jumps during the cooldown
- Once the cooldown completes, the double jump becomes available again

### Jump Mechanics
- **Regular Jump**: Press jump key while on ground → normal jump
- **Double Jump**: Press jump key while in air (during cooldown period) → second jump with same height
- **Landing**: When you land, the double jump ability resets, allowing another use after the cooldown

## Visual Feedback

### UI Indicator (Top Right Corner)
The double jump status is displayed with an icon showing:

#### When Ready (BLUE):
- Two vertical arrows pointing upward with a pulsing glow effect
- Label shows **"READY"**
- The icon glows and pulses to grab attention

#### During Cooldown (RED):
- Cooldown timer displaying remaining time (e.g., "3.2s")
- Progress bar filling from left to right as cooldown decreases
- Label shows **"COOLDOWN"**

### Particle Effects
- When you perform a double jump, **25 spark particles** burst outward
- These particles create a visual explosion effect at your position
- Adds satisfying visual feedback for using the ability

## Gameplay Features

### Strategic Use
- Use double jumps to avoid obstacles in difficult situations
- Plan your double jump timing to escape last-minute collisions
- The 10-second cooldown encourages thoughtful, strategic jumping

### Resets
- Double jump ability resets when you land on the ground
- The 10-second cooldown timer is independent of landing
- You can always land and jump again, even during cooldown

### Integration
- Double jump works with all game states
- Compatible with touch/on-screen JUMP button
- Sound effect plays when double jump is performed
- Counts as a regular jump for score purposes

## Technical Implementation

### Player Class Updates
```python
# New properties added:
self.double_jump_available = True
self.double_jump_cooldown = 600  # 10 seconds at 60 FPS
self.double_jump_cooldown_timer = 0
self.can_double_jump = False  # Can only use once per air session

# New methods:
def double_jump(self):
    # Performs the double jump if conditions are met
    # Returns True if successful, False otherwise
```

### Controls
- **SPACE / UP ARROW / W**: Jump or Double Jump
- **P**: Pause game
- **R**: Restart after game over
- **M**: Return to menu from game over

## Tips for Players

1. **Timing is Everything**: Double jumps are most useful when you're about to hit an obstacle
2. **Plan Ahead**: Since there's a cooldown, use double jumps wisely
3. **Backup Plans**: Don't rely solely on double jump - practice regular jumping too
4. **Watch the Indicator**: Keep an eye on the double jump icon to know when it's ready

## Balance

The 10-second cooldown ensures the game remains challenging:
- You get one powerful defensive tool per 10 seconds
- Regular jumps are still the primary movement mechanic
- The feature adds skill expression without making the game trivial
- Cooldown encourages spacing out double jump uses strategically

Enjoy your enhanced jumping abilities! 🚀
