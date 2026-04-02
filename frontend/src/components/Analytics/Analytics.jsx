import React from 'react';
import { Typography, Box, Paper } from '@mui/material';

function Analytics() {
  return (
    <Box>
      <Typography variant="h4" gutterBottom>Analytics</Typography>
      <Paper sx={{ p: 3 }}>
        <Typography variant="body1">
          Detailed analytics and performance metrics will be displayed here.
        </Typography>
      </Paper>
    </Box>
  );
}

export default Analytics;
