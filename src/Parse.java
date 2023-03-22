import java.util.HashSet;
import java.util.Scanner;

public class Parse{
    public static final int PROPERTY_KEY = 0;
    public static final int PROPERTY_ID = 1;
    public static final int PROPERTY_COL = 2;
    public static final int PROPERTY_ROW = 3;
    public static final int ENTITY_NUM_PROPERTIES = 4;

    private static void parseCow(WorldModel world, String[] properties, Point pt, String id, ImageStore imageStore) {
        if (properties.length == Cow.COW_NUM_PROPERTIES) {
            Entity entity = Cow.createCow(id, pt, Double.parseDouble(properties[Cow.COW_ACTION_PERIOD]), Double.parseDouble(properties[Cow.COW_ANIMATION_PERIOD]), Integer.parseInt(properties[Cow.COW_LIMIT]), imageStore.getImageList(Cow.COW_KEY));
            world.tryAddEntity(entity);
        } else {
            throw new IllegalArgumentException(String.format("%s requires %d properties when parsing", Cow.COW_KEY, Cow.COW_NUM_PROPERTIES));
        }
    }
    public static void parseSapling(WorldModel world, String[] properties, Point pt, String id, ImageStore imageStore) {
        if (properties.length == Sapling.SAPLING_NUM_PROPERTIES) {
            int health = Integer.parseInt(properties[Sapling.SAPLING_HEALTH]);
            Entity entity = new Sapling(id, pt, imageStore.getImageList(Sapling.SAPLING_KEY), health);
            world.tryAddEntity(entity);
        }else{
            throw new IllegalArgumentException(String.format("%s requires %d properties when parsing", Sapling.SAPLING_KEY, Sapling.SAPLING_NUM_PROPERTIES));
        }
    }

    public static void parseDude(WorldModel world, String[] properties, Point pt, String id, ImageStore imageStore) {
        if (properties.length == Dude.DUDE_NUM_PROPERTIES) {
            Entity entity = DudeNotFull.createDudeNotFull(id, pt, Double.parseDouble(properties[Dude.DUDE_ACTION_PERIOD]), Double.parseDouble(properties[Dude.DUDE_ANIMATION_PERIOD]), Integer.parseInt(properties[Dude.DUDE_LIMIT]), imageStore.getImageList(Dude.DUDE_KEY));
            world.tryAddEntity(entity);
        }else{
            throw new IllegalArgumentException(String.format("%s requires %d properties when parsing", Dude.DUDE_KEY, Dude.DUDE_NUM_PROPERTIES));
        }
    }

    public static void parseFairy(WorldModel world, String[] properties, Point pt, String id, ImageStore imageStore) {
        if (properties.length == Fairy.FAIRY_NUM_PROPERTIES) {
            Entity entity = new Fairy(id, pt, Double.parseDouble(properties[Fairy.FAIRY_ACTION_PERIOD]), Double.parseDouble(properties[Fairy.FAIRY_ANIMATION_PERIOD]), imageStore.getImageList(Fairy.FAIRY_KEY));
            world.tryAddEntity(entity);
        }else{
            throw new IllegalArgumentException(String.format("%s requires %d properties when parsing", Fairy.FAIRY_KEY, Fairy.FAIRY_NUM_PROPERTIES));
        }
    }

    public static void parseTree(WorldModel world, String[] properties, Point pt, String id, ImageStore imageStore) {
        if (properties.length == Tree.getTreeNumProperties()) {
            Entity entity = Tree.createTree (id, pt, Double.parseDouble(properties[Tree.getTreeActionPeriod()]), Double.parseDouble(properties[Tree.getTreeAnimationPeriod()]), Integer.parseInt(properties[Tree.getTreeHealth()]), imageStore.getImageList(Tree.getTreeKey()));
            world.tryAddEntity(entity);
        }else{
            throw new IllegalArgumentException(String.format("%s requires %d properties when parsing", Tree.getTreeKey(), Tree.getTreeNumProperties()));
        }
    }

    public static void parseObstacle(WorldModel world, String[] properties, Point pt, String id, ImageStore imageStore) {
        if (properties.length == Obstacle.OBSTACLE_NUM_PROPERTIES) {
            Entity entity = new Obstacle (id, pt, Double.parseDouble(properties[Obstacle.OBSTACLE_ANIMATION_PERIOD]), imageStore.getImageList(Obstacle.OBSTACLE_KEY));
            world.tryAddEntity(entity);
        }else{
            throw new IllegalArgumentException(String.format("%s requires %d properties when parsing", Obstacle.OBSTACLE_KEY, Obstacle.OBSTACLE_NUM_PROPERTIES));
        }
    }

    public static void parseHouse(WorldModel world, String[] properties, Point pt, String id, ImageStore imageStore) {
        if (properties.length == House.HOUSE_NUM_PROPERTIES) {
            Entity entity = House.createHouse (id, pt, imageStore.getImageList(House.HOUSE_KEY));
            world.tryAddEntity(entity);
        }else{
            throw new IllegalArgumentException(String.format("%s requires %d properties when parsing", House.HOUSE_KEY, House.HOUSE_NUM_PROPERTIES));
        }
    }

    public static void parseStump(WorldModel world, String[] properties, Point pt, String id, ImageStore imageStore) {
        if (properties.length == Stump.STUMP_NUM_PROPERTIES) {
            Entity entity = new Stump (id, pt, imageStore.getImageList(Stump.STUMP_KEY));
            world.tryAddEntity(entity);
        }else{
            throw new IllegalArgumentException(String.format("%s requires %d properties when parsing", Stump.STUMP_KEY, Stump.STUMP_NUM_PROPERTIES));
        }
    }

    public static void parseSaveFile(WorldModel world, Scanner saveFile, ImageStore imageStore, Background defaultBackground){
        String lastHeader = "";
        int headerLine = 0;
        int lineCounter = 0;
        while(saveFile.hasNextLine()){
            lineCounter++;
            String line = saveFile.nextLine().strip();
            if(line.endsWith(":")){
                headerLine = lineCounter;
                lastHeader = line;
                switch (line){
                    case "Backgrounds:" -> world.setBackground(new Background[world.getNumRows()][world.getNumCols()]);
                    case "Entities:" -> {
                        world.setOccupancy(new Entity[world.getNumRows()][world.getNumCols()]);
                        world.setEntities(new HashSet<>());
                    }
                }
            }else{
                switch (lastHeader){
                    case "Rows:" -> world.setNumRows(Integer.parseInt(line));
                    case "Cols:" -> world.setNumCols(Integer.parseInt(line));
                    case "Backgrounds:" -> Parse.parseBackgroundRow(world, line, lineCounter-headerLine-1, imageStore);
                    case "Entities:" -> Parse.parseEntity(world, line, imageStore);
                }
            }
        }
    }

    public static void parseBackgroundRow(WorldModel world, String line, int row, ImageStore imageStore) {
        String[] cells = line.split(" ");
        if(row < world.getNumRows()){
            int rows = Math.min(cells.length, world.getNumCols());
            for (int col = 0; col < rows; col++){
                world.getBackground()[row][col] = new Background(cells[col], imageStore.getImageList(cells[col]));
            }
        }
    }

    public static void parseEntity(WorldModel world, String line, ImageStore imageStore) {
        String[] properties = line.split(" ", Parse.ENTITY_NUM_PROPERTIES + 1);
        if (properties.length >= Parse.ENTITY_NUM_PROPERTIES) {
            String key = properties[PROPERTY_KEY];
            String id = properties[Parse.PROPERTY_ID];
            Point pt = new Point(Integer.parseInt(properties[Parse.PROPERTY_COL]), Integer.parseInt(properties[Parse.PROPERTY_ROW]));

            properties = properties.length == Parse.ENTITY_NUM_PROPERTIES ?
                    new String[0] : properties[Parse.ENTITY_NUM_PROPERTIES].split(" ");

            switch (key) {
                case Cow.COW_KEY -> Parse.parseCow(world, properties, pt, id, imageStore);
                case Obstacle.OBSTACLE_KEY -> Parse.parseObstacle(world, properties, pt, id, imageStore);
                case Dude.DUDE_KEY -> Parse.parseDude(world, properties, pt, id, imageStore);
                case Fairy.FAIRY_KEY -> Parse.parseFairy(world, properties, pt, id, imageStore);
                case House.HOUSE_KEY -> Parse.parseHouse(world, properties, pt, id, imageStore);
                case Tree.TREE_KEY -> Parse.parseTree(world, properties, pt, id, imageStore);
                case Sapling.SAPLING_KEY -> Parse.parseSapling(world, properties, pt, id, imageStore);
                case Stump.STUMP_KEY -> Parse.parseStump(world, properties, pt, id, imageStore);
                default -> throw new IllegalArgumentException("Entity key is unknown");
            }
        }else{
            throw new IllegalArgumentException("Entity must be formatted as [key] [id] [x] [y] ...");
        }
    }
}