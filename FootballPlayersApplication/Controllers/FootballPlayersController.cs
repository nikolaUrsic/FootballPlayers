using FootballPlayersApplication.Models;
using System.Collections.Generic;
using System.Linq;
using System.Web.Http;

namespace FootballPlayersApplication.Controllers
{
    public class FootballPlayersController : ApiController
    {
        public IHttpActionResult Get()
        {
            IList<FootballPlayer> players = new List<FootballPlayer>();
            using (FootballPlayersDatabaseEntities entities = new FootballPlayersDatabaseEntities())
            {
                players = entities.FootballPlayers.ToList();
            }
            if (players.Count == 0)
            {
                return NotFound();
            }
            return Ok(players);
        }

        public IHttpActionResult Get(int id)
        {
            FootballPlayer player = null;
            using (FootballPlayersDatabaseEntities entities = new FootballPlayersDatabaseEntities())
            {
                player = entities.FootballPlayers.FirstOrDefault(e => e.Id == id);
            }
            if (player == null)
            {
                return NotFound();
            }
            return Ok(player);
        }

        public IHttpActionResult Post([FromBody]FootballPlayer player)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest("Indalid data");
            }
            if (player.Id != 0)
            {
                return BadRequest("You can not define football player's id");
            }
            using (FootballPlayersDatabaseEntities entities = new FootballPlayersDatabaseEntities())
            {
                entities.FootballPlayers.Add(new FootballPlayer()
                {
                    FirstName = player.FirstName,
                    LastName = player.LastName,
                    Age = player.Age,
                    FieldPosition = player.FieldPosition
                });
                entities.SaveChanges();
            }
            return Ok();
        }

        public IHttpActionResult Put([FromBody]FootballPlayer player)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest("Indalid data");
            }
            using (FootballPlayersDatabaseEntities entities = new FootballPlayersDatabaseEntities())
            {
                var existingPlayer = entities.FootballPlayers.FirstOrDefault(e => e.Id == player.Id);
                if (existingPlayer == null)
                {
                    return NotFound();
                }
                existingPlayer.FirstName = player.FirstName; 
                existingPlayer.LastName = player.LastName;
                existingPlayer.Age = player.Age;
                existingPlayer.FieldPosition = player.FieldPosition;
                entities.SaveChanges();
            }
            return Ok();
        }

        public IHttpActionResult Delete(int id)
        {
            if (id <= 0)
            {
                return BadRequest("Indalid id");
            }
            using (FootballPlayersDatabaseEntities entities = new FootballPlayersDatabaseEntities())
            {
                var existingPlayer = entities.FootballPlayers.FirstOrDefault(e => e.Id == id);
                if (existingPlayer == null)
                {
                    return NotFound();
                }
                entities.Entry(existingPlayer).State = System.Data.Entity.EntityState.Deleted;
                entities.SaveChanges();
                return Ok();
            }
        }
    }
}
