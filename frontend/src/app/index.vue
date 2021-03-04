<template>
<div :class="'app'">
	<NavBar></NavBar>
	<KanbanBoard></KanbanBoard>
	<!-- <router-view></router-view> -->
</div>
</template>

<script>
import { KanbanBoard } from './components';
import { NavBar } from './components';



export default {
	name: "App",
	components: {
		KanbanBoard,
		NavBar
	} 
};
</script>

<style src="../style.css"/>

