<template>
<div :class="'app'">
	<NavBar></NavBar>
	<router-view></router-view>	
	<!-- <KanbanBoard></KanbanBoard> -->
</div>
</template>

<script>
// import { KanbanBoard } from './components';
import { NavBar } from './components';
// import { Signin } from './components';




export default {
	name: "App",
	components: {
		// KanbanBoard,
		NavBar
	},
	
};
</script>

<style src="../style.css"/>

