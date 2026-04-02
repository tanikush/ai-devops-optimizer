import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { AppBar, Toolbar, Typography, Container, Box, Drawer, List, ListItem, ListItemIcon, ListItemText, CssBaseline } from '@mui/material';
import DashboardIcon from '@mui/icons-material/Dashboard';
import TimelineIcon from '@mui/icons-material/Timeline';
import PredictIcon from '@mui/icons-material/Psychology';
import RecommendIcon from '@mui/icons-material/Lightbulb';
import PipelineIcon from '@mui/icons-material/AccountTree';

import Dashboard from './components/Dashboard/Dashboard';
import PipelineList from './components/PipelineList/PipelineList';
import Analytics from './components/Analytics/Analytics';
import Predictions from './components/Predictions/Predictions';
import Recommendations from './components/Recommendations/Recommendations';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

const drawerWidth = 240;

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Box sx={{ display: 'flex' }}>
          <AppBar position="fixed" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
            <Toolbar>
              <Typography variant="h6" noWrap component="div">
                AI DevOps Pipeline Optimizer
              </Typography>
            </Toolbar>
          </AppBar>
          
          <Drawer
            variant="permanent"
            sx={{
              width: drawerWidth,
              flexShrink: 0,
              '& .MuiDrawer-paper': {
                width: drawerWidth,
                boxSizing: 'border-box',
              },
            }}
          >
            <Toolbar />
            <Box sx={{ overflow: 'auto' }}>
              <List>
                <ListItem button component={Link} to="/">
                  <ListItemIcon><DashboardIcon /></ListItemIcon>
                  <ListItemText primary="Dashboard" />
                </ListItem>
                <ListItem button component={Link} to="/pipelines">
                  <ListItemIcon><PipelineIcon /></ListItemIcon>
                  <ListItemText primary="Pipelines" />
                </ListItem>
                <ListItem button component={Link} to="/analytics">
                  <ListItemIcon><TimelineIcon /></ListItemIcon>
                  <ListItemText primary="Analytics" />
                </ListItem>
                <ListItem button component={Link} to="/predictions">
                  <ListItemIcon><PredictIcon /></ListItemIcon>
                  <ListItemText primary="Predictions" />
                </ListItem>
                <ListItem button component={Link} to="/recommendations">
                  <ListItemIcon><RecommendIcon /></ListItemIcon>
                  <ListItemText primary="Recommendations" />
                </ListItem>
              </List>
            </Box>
          </Drawer>
          
          <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
            <Toolbar />
            <Container maxWidth="xl">
              <Routes>
                <Route path="/" element={<Dashboard />} />
                <Route path="/pipelines" element={<PipelineList />} />
                <Route path="/analytics" element={<Analytics />} />
                <Route path="/predictions" element={<Predictions />} />
                <Route path="/recommendations" element={<Recommendations />} />
              </Routes>
            </Container>
          </Box>
        </Box>
      </Router>
    </ThemeProvider>
  );
}

export default App;
