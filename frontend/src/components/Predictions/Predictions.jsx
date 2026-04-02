import React from 'react';
import { Typography, Box, Paper } from '@mui/material';

function Predictions() {
  return (
    <Box>
      <Typography variant="h4" gutterBottom>Predictions</Typography>
      <Paper sx={{ p: 3 }}>
        <Typography variant="body1">
          AI-powered build failure predictions and duration estimates will be displayed here.
        </Typography>
      </Paper>
    </Box>
  );
}

export default Predictions;
