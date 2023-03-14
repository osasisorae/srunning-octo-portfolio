import React, { useState, useEffect } from "react";
import { makeStyles } from 'tss-react/mui'
import {
  Avatar,
  Card,
  CardContent,
  CardHeader,
  Divider,
  List,
  ListItem,
  ListItemAvatar,
  ListItemText,
  Typography,
} from "@mui/material";

const useStyles = makeStyles((theme) => ({
  root: {
    maxWidth: 800,
    margin: "auto",
    marginTop: theme.spacing(4),
  },
  cardHeader: {
    textAlign: "center",
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.common.white,
  },
  projectsHeader: {
    marginBottom: theme.spacing(1),
    marginTop: theme.spacing(4),
  },
}));

function Home() {
  const classes = useStyles();
  const [user, setUser] = useState({
    username: 'osasisorae',
    email: 'osasisorae@gmail.com',
    first_name: 'Osarenren',
    last_name: 'Isorae',
  });

  const [projects, setProjects] = useState([]);


  useEffect(() => {
    // Fetch projects data
    fetch("http://127.0.0.1:8000/api/v1/projects/")
      .then((res) => res.json())
      .then((data) => {
        setProjects(data);})
      .catch(error => console.error(error));
  }, []);

  return (
    <div className={classes.root}>
      {user && (
        <Card>
          <CardHeader
            className={classes.cardHeader}
            avatar={<Avatar>{user.username.charAt(0)}</Avatar>}
            title={user.first_name + " " + user.last_name}
            subheader={user.email}
          />
          <CardContent>
            <Typography variant="h5" component="h2">
              About me
            </Typography>
            <Typography variant="body1" component="p">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla
              elementum sapien vel justo imperdiet ullamcorper. Suspendisse
              potenti. Nulla facilisi. Nulla facilisi. Nulla malesuada libero
              tellus, eu tincidunt arcu pretium eu. Donec ornare ligula at
              libero volutpat euismod.
            </Typography>
            <Divider className={classes.projectsHeader} />
            <Typography
              variant="h5"
              component="h2"
              className={classes.projectsHeader}
            >
              Projects
            </Typography>
            <List>
                {projects && projects.map((project) => (
                    <ListItem key={project.id}>
                    <ListItemAvatar>
                        <Avatar>{project.title.charAt(0)}</Avatar>
                    </ListItemAvatar>
                    <ListItemText
                        primary={project.title}
                        secondary={
                        "From " +
                        new Date(project.start_date).toLocaleDateString() +
                        " to " +
                        new Date(project.end_date).toLocaleDateString()
                        }
                    />
                    </ListItem>
              ))}
            </List>
          </CardContent>
        </Card>
      )}
    </div>
  );
}

export default Home;
